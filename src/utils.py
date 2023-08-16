import itertools
import re
from difflib import SequenceMatcher
from functools import cache

import numpy as np
import pandas as pd
from gensim.models import fasttext

from src import (
    LENNY_FACE_FILTER,
    LINK_FILTER,
    MASKED_PROFANITY_REGEX,
    MODEL_DIR,
    NICKNAMES_FILTER,
    ONE_CHANGED_REGEX,
    PROF_DF,
)

ft_model = fasttext.load_facebook_model(MODEL_DIR / "cc.pl.300.bin")
ALL_WORDS = tuple(ft_model.wv.key_to_index.keys())

from src import POPULAR_CHANGES, POPULAR_SIGNS


def similar(a: str, b: str) -> float:
    """Count similarities of 2 strings.
    Similarity is counted by comparing strings char by char.

    Args:
        a (str): 1st string for comparison
        b (str): 2nd string for comparison

    Returns:
        float: Value between 0 and 1 - similarity between strings.
    """
    return SequenceMatcher(None, a, b).ratio()


def get_profanity(prof_df: pd.DataFrame, masked_word: str) -> str:
    """Unmask profanity in which masked part is masked by random sequance, eg.:
    * k%^$%^wa -> kurwa
    * pi&^*^&le -> pierdole
    * p?*@%da -> pizda
    Args:
        prof_df (pd.DataFrame): Dataframe containing polish profanities
        masked_word (str): Masked profanity.

    Raises:
        ValueError: If algorithm can't find actual profanity, raise an error.

    Returns:
        str: Unmasked profanity.
    """
    prof_df["sim"] = prof_df["profanity"].apply(
        lambda x: similar(x, masked_word.lower())
    )
    alternative_words = prof_df.sort_values("sim", ascending=False)
    try:
        start, end = re.sub("[^a-żA-ż]+", " ", masked_word).split()
    except ValueError:
        try:
            result = re.sub("[^a-żA-ż]+", " ", masked_word).split()
            start, end = result[0], result[-1]
        except ValueError:
            start = re.sub("[^a-żA-ż]+", " ", masked_word).split()[0]
            end = ""
    alternative_words["is_ok_start"] = alternative_words["profanity"].apply(
        lambda x: x.startswith(start)
    )
    alternative_words["is_ok_end"] = alternative_words["profanity"].apply(
        lambda x: x.endswith(end)
    )
    both_ok = alternative_words[
        alternative_words["is_ok_start"] & alternative_words["is_ok_end"]
    ]
    start_ok = alternative_words[alternative_words["is_ok_start"]]
    end_ok = alternative_words[alternative_words["is_ok_end"]]

    if not both_ok.empty:
        new_word = both_ok.iloc[0, 0]
    elif not start_ok.empty and end == "":
        new_word = start_ok.iloc[0, 0]
    elif not end_ok.empty and end != "" and start == "":
        new_word = end_ok.iloc[0, 0]
    else:
        raise ValueError(
            "Incorrect values catched by regex or word is not in prafinities dictionary."
        )
    return new_word


@cache
def replace_word(unknown: str, words: list) -> str:
    """Replace masked word with its actual form.

    Args:
        unknown (str): Masked word.
        words (list): List of possible words available in given language.

    Returns:
        str: Unmasked word.
    """

    # find possible options
    symbols = re.findall(POPULAR_SIGNS, unknown)
    options = {
        item: [key for key in POPULAR_CHANGES if item in POPULAR_CHANGES[key]]
        for item in symbols
    }

    # find list of possible words based on start and end of the word
    start = unknown[: unknown.find(symbols[0])]
    end = unknown[unknown.find(symbols[-1]) + 1 :]
    sim_words = [
        word
        for word in words
        if word.startswith(start) and word.endswith(end) and len(word) == len(unknown)
    ]

    if len(sim_words) == 0:
        return unknown
    elif len(sim_words) == 1:
        return sim_words[0]
    else:
        # if there is more than one possiible words create all possibilities
        # based on popular changes (i->1, e->3 ect.) and choose one existing in dictionary
        # eg. p3n1$ gets following possibilities: [penis, peniś, penls, penlś] but only
        # first one exists in dicitonary
        potencial_words = []
        for option in itertools.product(*options.values()):
            known = unknown
            for i in range(len(option)):
                known = known.replace(symbols[i], option[i])
            potencial_words.append(known)

        exact_words = list(set(sim_words).intersection(potencial_words))

        if len(exact_words) == 0:
            df = pd.DataFrame({"words": sim_words})
            for word in potencial_words:
                df[word] = df["words"].apply(lambda x: similar(x, word))
            df.set_index("words", inplace=True)

            max_val = df.max().max()
            best_word = (
                (df == max_val).replace(False, np.nan).dropna(how="all").index[0]
            )

            return best_word

        else:
            return exact_words[0]


def unmask_profanities(text: str) -> str:
    """Unmask profanities and any words where letter was replaced with sign. eg.:
    * pi3&!lić -> pierdolić
    * k&^$wa -> kurwa
    * s3ks -> seks
    * p0lak -> polak
    Args:
        text (str): Masked text.

    Returns:
        str: Text with unmasked profanities.
    """
    # replace masked profanities, eg. 'pi3&!lić
    prof_in_text = re.findall(MASKED_PROFANITY_REGEX, text)

    for item in prof_in_text:
        try:
            new_word = get_profanity(PROF_DF, item)
            text = text.replace(item, new_word)
        except ValueError:
            continue

    # replace one letter changed eg. pi3rdolić
    pattern = "|".join(re.findall(ONE_CHANGED_REGEX, text))
    if pattern:
        words = [word for word in text.split() if bool(re.match(pattern, word))]
        for word in words:
            if text.find(word) == 0:
                before = ""
            else:
                before = text[text.find(word) - 1]
            new_word = replace_word(word, ALL_WORDS)
            # avoid replacing usernames
            if before != "@" and word != new_word:
                text = text.replace(word, new_word)

    return text


def clean_text(
    text: str,
    masked_profanity: bool = False,
    filter_link: bool = False,
    filter_lennyface: bool = False,
    filter_hashtags: bool = False,
    filter_nicknames: bool = False,
) -> str:
    """Clean text - remove nicknames, links, lennyfaces.

    Args:
        text (str): Text to clean.
        masked_profanity (bool): Should profanities be unmasked?
        filter_link (bool): Should links be removed?
        filter_lennyface (bool): Should lennyface be removed?
        filter_hashtags (bool): Should hashtags be removed?
        filter_nicknames (bool): Should nicknames be removed?
    Returns:
        str: Clean version of text.
    """

    # filter lenny faces and https and sources
    source = text.lower().find("źródło:")

    if source != -1:
        text = text[:source]

    if filter_link:
        text = re.sub(LINK_FILTER, " ", text)
        text = text.replace("{URL}", " ")

    if filter_lennyface:
        text = re.sub(LENNY_FACE_FILTER, " ", text)

    if filter_hashtags:
        text = re.sub("#\S+", " ", text)

    if masked_profanity:
        text = unmask_profanities(text)

    if filter_nicknames:
        text = re.sub(NICKNAMES_FILTER, " ", text)
    if filter_lennyface or filter_link:
        text = re.sub("[\[\]<>()]|\*\*", " ", text)

    # remove duplicated white spaces
    text = text.split()
    text = " ".join(text)

    return text

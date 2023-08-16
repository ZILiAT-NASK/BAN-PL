from pathlib import Path

import pandas as pd

# Directories
MAIN_DIR = Path(__file__).parent.parent.resolve()
DATA_DIR = MAIN_DIR / "data"
MODEL_DIR = MAIN_DIR / "models"

LINK_FILTER = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
LENNY_FACE_FILTER = "[•́̀￣ݓ✖･՞﹒︣⌣⁰❛¯͒´`ཀ༎ຶຈO͡◕͠°⇀↼ಥ☯͝ಠೃರ˙◔□⌐▀・◉‾⊙◐◖◗◑ヘ¬≖̿ิʘ̆☉;■º͜’^–xᴼ＾˘۞◯๑ᵔσ✪♥ั╥ᵒ̌ಡ̲ᵕିୖଵ்౦್രිᓀᓂ⊡⊚⊘⊗¤☢⚆☭◪Ɵ].{0,4}[_ਊ︿〜〰∧Д۝ڡʖ͜ل‸⌂͟﹏益‿̯Ĺʟдᗜᴥω◞౪◟෴ुرں┏┓ヮ▽▃ₒ̀ε~□◡3◯̫╭╮()▾＊ⓞ].{0,4}[•́̀￣ݓ✖･՞﹒︣⌣⁰❛¯͒´`ཀ༎ຶຈO͡◕͠°⇀↼ಥ☯͝ಠೃರ˙◔□⌐▀・◉‾⊙◐◖◗◑ヘ¬≖̿ิʘ̆☉;■º͜’^–xᴼ＾˘۞◯๑ᵔσ✪♥ั╥ᵒ̌ಡ̲ᵕିୖଵ்౦್രිᓀᓂ⊡⊚⊘⊗¤☢⚆☭◪Ɵ]"
MASKED_PROFANITY_REGEX = "[A-Ża-ż]+[\*+|\!+|\?+|\.+|#+|@+|\$+|%+|\^+|&+]{2,}[A-Ża-ż]+|[A-Ża-ż]+\*+[A-Ża-ż]+|[A-Ża-ż]+(?=[\*+|#+|@+|\$+|%+|\^+|&+])[\*+|#+|@+|\$+|%+|\^+|&+]{2,}"
NICKNAMES_FILTER = "\*\*.+\*\*:\s|@\S+:\s| @\S+|\{USERNAME\}: |\{USERNAME\}"
ONE_CHANGED_REGEX = "[a-żA-Ż]+[8|4|3|@|q|!|$|0|1]+[a-żA-Ż|8|4|3|@|!|$|0|1]*"
POPULAR_SIGNS = "[8|4|3|@|q|!|$|0|1]"
POPULAR_CHANGES = {
    "i": ["&", "1", "!"],
    "a": ["@", "4"],
    "e": ["3"],
    "l": ["1", "!"],
    "s": ["$", "5"],
    "ś": ["$"],
    "o": ["0"],
    "z": ["2"],
    "b": ["8"],
    "ku": ["q"],
    "k": ["q"],
}

PROF_DF = pd.read_csv(DATA_DIR / "polish_vulgarisms_extended.txt", names=["profanity"])
PROFANITY_REGEX = "|".join(PROF_DF.values.flatten())

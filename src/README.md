## IMPORTANT!
Please download fasttext model from [here](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pl.300.bin.gz) and save it in `models` folder. 

# Code usage 🧑‍💻

We have prepared two functions to be used when working with data. 

1. `unmask_profanities` – unmasks profanities and any words where one or more letters were replaced with a sign, e.g.:
    * pi3&!lić -> pierdolić,
    * k&^$wa -> kurwa,
    * s3ks -> seks,
    * p0lak -> polak.

2. `clean_text` – unmasks profanities and removes any of the following:
    * links,
    * lennyfaces,
    * hashtags,
    * nicknames.
    
    In the `clean_text` function all actions are optional. 

## Usage:
1. `unmask_profanities`:

    [In]:
    ```python
    to_unmask = ['ku**a', 'pier*olnięty', 'odp#$!$%?ić', 'k0nfiarska', 'Jeb@na',
        'P0lki']

    for word in to_unmask:
        print(f"{word} -> {unmask_profanities(word)}")
    ```

    [Out]:
    ```ku**a -> kurwa
    pier*olnięty -> pierdolnięty
    odp#$!$%?ić -> odpierdolić
    k0nfiarska -> konfiarska
    Jeb@na -> Jebana
    P0lki -> Polki
    ```

    Please be informed that some words (i.e., words that are not included in the dictionary such as `konfiarska`) can remain masked. Moreover, some masked words that fit to a couple of profanities (e.g., `jeb$#%&`) can be unmasked incorrectly. 

2. `clean_text`:

   [In]:
   ```python
   texts = [
       '@anonymous: ku**a ale z Ciebie debil ( ͡° ͜ʖ ͡°)',
       "@anonymous: moje kilka ostatnich spadło, on już nawet nie zgłasza jak się pisze jego dane, wystarczy napisać w kontekście uniwersum co by zrobił 'pier*olnięty' i już leci zgłoszenie, śmiechu warte",
       '@anonymous    Proszę odp#$!$%?ić od podkarpackiej wsi i wracać do swojej mazowieckiej wsi, buraku obsrany',
       '@anonymous  k0nfiarska trollownia - "internetowy oddział Nowy Sącz" pod przewodnictwem egipskiego mariuszka udającego babę i podrywającego przegrywów (jednocześnie będąc narolem) rozrósł się w roku wyborczym...',
       '@anonymous: właśnie wiąże pętlę, żegnajcie(╯︵╰,)\nJeb@na idiotka',
       '@anonymous: płeć empatyczna. P0lki to coorvy'
   ]
   
   for text in texts:
       print(f"Original: {text}", f"Cleaned: {clean_text(text, True, True, True, True, True)}", 
             sep='\n'+'-'*70+'\n', end='\n'+'='*70+'\n')
   ```
   [Out]:
   ```
   Original: @anonymous: ku**a ale z Ciebie debil ( ͡° ͜ʖ ͡°)
   ----------------------------------------------------------------------
   Cleaned: kurwa ale z Ciebie debil
   ======================================================================
   Original: @anonymous: moje kilka ostatnich spadło, on już nawet nie zgłasza jak się pisze jego dane, wystarczy napisać w kontekście uniwersum co by zrobił 'pier*olnięty' i już leci zgłoszenie, śmiechu warte
   ----------------------------------------------------------------------
   Cleaned: moje kilka ostatnich spadło, on już nawet nie zgłasza jak się pisze jego dane, wystarczy napisać w kontekście uniwersum co by zrobił 'pierdolnięty' i już leci zgłoszenie, śmiechu warte
   ======================================================================
   Original: @anonymous    Proszę odp#$!$%?ić od podkarpackiej wsi i wracać do swojej mazowieckiej wsi, buraku obsrany
   ----------------------------------------------------------------------
   Cleaned: @anonymous Proszę odp od podkarpackiej wsi i wracać do swojej mazowieckiej wsi, buraku obsrany
   ======================================================================
   Original: @anonymous  k0nfiarska trollownia - "internetowy oddział Nowy Sącz" pod przewodnictwem egipskiego mariuszka udającego babę i podrywającego przegrywów (jednocześnie będąc narolem) rozrósł się w roku wyborczym...
   ----------------------------------------------------------------------
   Cleaned: @anonymous k0nfiarska trollownia - "internetowy oddział Nowy Sącz" pod przewodnictwem egipskiego mariuszka udającego babę i podrywającego przegrywów jednocześnie będąc narolem rozrósł się w roku wyborczym...
   ======================================================================
   Original: @anonymous: właśnie wiąże pętlę, żegnajcie(╯︵╰,)
   Jeb@na idiotka
   ----------------------------------------------------------------------
   Cleaned: właśnie wiąże pętlę, żegnajcie ╯︵╰, Jebana idiotka
   ======================================================================
   Original: @anonymous: płeć empatyczna. P0lki to coorvy
   ----------------------------------------------------------------------
   Cleaned: płeć empatyczna. Polki to coorvy
   ======================================================================

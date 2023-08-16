# BAN-PL: a Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service
![Thumbnail](https://github.com/ZILiAT-NASK/BAN-PL/tree/main/imgs/thumbnail.png)

The repository contains a comprehensive Polish language dataset that encompasses text samples flagged as harmful and subsequently removed by professional moderators. The dataset encompasses a total of 691,662 pieces of content from a popular social networking service, Wykop.pl, often referred to as the "Polish Reddit", including both posts and comments, and is evenly distributed into two distinct classes: "harmful" and "neutral".
This dataset was curated by the Department of Linguistic Engineering and Text Analysis at [NASK National Research Institute](https://science.nask.pl/en) in close collaboration with [Wykop.pl](https://wykop.pl/) as part of the [KOMTUR project](https://www.nask.pl/pl/projekty-dofinansowane/projekty-ue/5019,System-do-kategoryzacji-oceny-i-moderacji-tresci-internetowych-dla-nowych-uslug-.html) (*System for categorising, evaluating, and moderating online content for new services and advertising selection*).
The current version is v1.0. It contains 24,000 anonymized samples, of which 12,000 belong to the harmful class and 12,000 belong to the neutral class. More samples will be made available gradually. 

Detailed information regarding the BanHOff-PL dataset can be found in the paper [*BanHOff-PL: a Novel Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service*](link). 

**Caution: This dataset includes instances of text that may be deemed inappropriate, offensive, or distressing.**
Note: The purpose of this dataset is strictly for research and study purposes. It is imperative that this data is not employed in any operational or real-world applications unless accompanied by thorough filtering and oversight. The creators and collaborators of this dataset hold no responsibility for any misapplication or adverse outcomes arising from the utilization of this data. Users are accountable for adhering to all pertinent legal statutes and regulations concerning data utilization and confidentiality.

## Dataset description

### Data collection process

For the purpose of cyberbullying and offensive language detection, we included in the dataset both content banned for inciting hatred or violence (i.e., "Propagation of hatred or violence, drastic content," "Hatred or violence") and content containing personal attacks (i.e., "Attacks me or violates my personal rights," "Attacks me," "Attacks others"). In order to streamline the analysis and classification process, we have merged these categories into a single class labeled as "Offensive Content."  In addition to the aforementioned categories, we have also included content marked as "inappropriate". For this purpose, we performed an automated binary classification of the "inappropriate" content and included the observations classified as harmful in the dataset. 

To obtain a balanced dataset for the binary classification task, the contrasting neutral class was gathered from the main page of the web service. Only entries and comments published at least 48 hours prior to scraping were considered, taking into account the moderation dynamics of the platform. 

The “harmful” class was compiled over a period ranging from June 2013 to June 2023, with a significant portion of the data published specifically between June 2013 and August 2020. The "neutral" class was collected between March and August 2021, between June and November 2022, and between January and June 2023.

For token statistics by class see the table below:

![Statistics by class](https://github.com/ZILiAT-NASK/BAN-PL/tree/main/imgs/BAN_PL_stats.png)

### Data anonymization
Due to the presence of personal data, such as home and email addresses, phone numbers or identification numbers, within the dataset, a comprehensive anonymization approach was imperative. Usernames and hyperlinks have also been masked. In order to prevent the further spread of offensive content, the anonymization process also encompassed the surnames and pseudonyms of individuals targeted by such content. It has been decided that fictional characters, historical figures and deceased individuals are to remain non-anonymized. 

Sensitive information was replaced by the following tags: {USERNAME}, {URL}, [surname] (including user-modified ones and adjectives derived from surnames), [pseudonym], [address] (including street names, house numbers, postal codes), [email], [phonenumber], [number] (other numbers, e.g. PESEL). 

## Additional text cleaning
The released version of the dataset consists of raw data that underwent an anonymization procedure (removal of hyperlinks, usernames and masking of personal and sensitive data). For the additional text cleaning, we provide cleaning functions and regex expressions to remove the unwanted and redundant elements (e.g., lennyfaces and hashtags) and to unmask profanities. The text cleaning functions and regex expressions can be found [here](https://github.com/ZILiAT-NASK/BAN-PL/tree/main/src/utils.py).

## Disclaimer
It is important to acknowledge that certain comments featured within this dataset might have originally been part of a multi-modal content, involving not only textual elements but also accompanying images or videos. The absence of these supplementary modalities could potentially result in a misinterpretation of the initially prohibited textual content. We are dedicated to thorough data refinement efforts aimed at minimizing such instances.

Furthermore, we wish to highlight that, despite our meticulous manual annotation and verification processes, the anonymization procedure employed might not have achieved complete effectiveness. Some degree of errors or inaccuracies may persist despite our best efforts.

## Licence
The dataset and code in the repository are made available under a Creative Commons Attribution International 4.0 licence [(CC BY)](https://creativecommons.org/licenses/by/4.0/).

## Contact
Please contact the [Department of Linguistic Engineering and Text Analysis](mailto:ziliat@nask.pl?subject=[GitHub]%20BAN-PL%20Dataset) in case of any issues with the datasets.

## Citation
If you make use of this dataset, please cite the following paper.

```
bibtex
```

## Acknowledgment
The work was carried out within the KOMTUR project ("System for categorising, evaluating, and moderating online content for new services and advertising selection"), which was funded by the National Centre for Research and Development in Poland within the 3/1.1.1/2020 Operational Programme Smart Growth 2014–2020, co-financed with the European Regional Development Fund. 
The authors would like to thank the team from Wykop.pl, especially Paweł Ellerik and Andrzej Prałat, engaged in the project for cooperating on the corpus and patiently answering all the endless related questions as well as helping in the data collection.




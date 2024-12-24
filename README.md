# BAN-PL: a Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl Web Service

![Thumbnail](https://github.com/ZILiAT-NASK/BAN-PL/blob/main/imgs/thumbnail.png)

<h6> **Caution: This dataset includes instances of text that may be deemed inappropriate, offensive, or distressing.**
Note: The purpose of this dataset is strictly for research and study purposes. It is imperative that this data is not employed in any operational or real-world applications unless accompanied by thorough filtering and oversight. The creators and collaborators of this dataset hold no responsibility for any misapplication or adverse outcomes arising from the utilization of this data. Users are accountable for adhering to all pertinent legal statutes and regulations concerning data utilization and confidentiality. </h6>

**The repository contains the first publicly available dataset of offensive and harmful content banned from a web service Wykop.pl (often called the "Polish Reddit") by professional moderators.** Thanks to the Wykop owners, the banned posts and comments have been reclaimed and preprocessed for public usage. The current version of the dataset consists of **24 000 samples** of anonymized content, with **12 000 pieces for the "harmful"** and **12 000 for the "neutral" (non-harmful) class**. It is the first part of the entire set of about 700 000 samples that have been acquired but still need to be processed before launching. In the near future, we will continue to release further batches.

Wykop.pl has its internal moderation policy and resulting taxonomy, e.g., content inciting hatred or violence (i.e., "Propagation of hatred or violence, drastic content," "Hatred or violence") and content containing personal attacks (i.e., "Attacks me or violates my personal rights," "Attacks me," "Attacks others"). The first preprocessing step included joining these original moderation categories into one "harmful" type. 

The contrasting "neutral" class was collected from the main page of the web service. It includes only posts and comments older than at least 48 hours. The human moderation dynamics of the platform let us assume that the remaining (not banned) content after this period can be considered non-harmful.  

The "harmful" class encompasses entries and comments published between Q1 2019 to June 2023. The "neutral" type was collected between March and August 2021, between June and November 2022, and between January and June 2023.

*The password-protected data stored within a .zip file, along with the password itself, can be found [here](https://github.com/ZILiAT-NASK/BAN-PL/tree/main/data).*

## New release: Hate Speech Subcorpus
<img src="https://github.com/ZILiAT-NASK/BAN-PL/blob/main/imgs/HS.png" alt="HS" width="600">

Building on the release of the BAN-PL dataset, which contains offensive social media content, we sought to advance our research into a crucial and socially significant subcategory of hate speech. To construct a subcorpus that adheres to the **United Nations' definition of hate speech**, we employed a rigorous 2+1 annotation process.


United Nations defines hate speech as *any kind of communication in speech, writing or behaviour, that attacks or uses pejorative or discriminatory language with reference to a person or a group on the basis of who they are, in other words, based on their religion, ethnicity, nationality, race, colour, descent, gender or other identity factor.*

This definition was expanded upon in the detailed guidelines provided to the annotators. The annotation process involved **labeling 20,000 samples from the BAN-PL dataset, identifying 10% of posts and comments (2,000) as meeting the criteria for hate speech** (labeled as HS). Additionally, a separate label for **war-related content** (W) was introduced.

In light of recent military conflicts, particularly in Ukraine and Israel, we recognized the importance of distinguishing between hate speech and war-related comments. When war-related discourse escalated into extremist statements targeting entire nations or ethnic groups, annotators were instructed to classify the content as hate speech, provided that such motivations are rooted in nationality or ethnicity-based grounds.

However, many instances of social media content, despite employing offensive or hateful language, focused on criticizing military actions rather than stigmatizing entire nations or ethnicities. To address this nuance, we introduced the war-related label (W) to capture this type of content.

Depending on specific needs, researchers working with the dataset can choose to use or ignore the war-related class. We believe this flexible approach will enhance the utility of the dataset and contribute meaningfully to the broader research community.

**The release of the Hate speech subcorpus includes:**
- **2000 samples labeled as “hate speech” (HS)**
- **263 samples labeled as war-related (W)**

*The password-protected data stored within a .zip file, along with the password itself, can be found here.*


## Anonymization

To avoid reviving and spreading content once rightfully banned, we spent dozens of hours on human-checked anonymization of the data. The anonymization process included the surnames and pseudonyms of individuals, address details, URLS, ID, telephone numbers, and usernames mentioned in the conversations. 
However, to preserve as much as possible of the original style for the research and model training purposes, we decided to maintain names or sensitive-alike information of fictional characters, historical figures, and deceased individuals. Ethnic groups, companies, and political parties, i.e., non-individual groups addressed in the samples, also remain unchanged.  

The anonymized sensitive information was replaced by the following tags: {USERNAME}, {URL}, [surname] (including user-modified ones and adjectives derived from surnames), [pseudonym], [address] (including street names, house numbers, postal codes), [email], [phonenumber], [number] (other numbers, e.g. PESEL). 

## Accompanying scripts 

We provide cleaning functions and regex expressions if you wish to apply further text cleanings, such as removing unwanted and redundant elements (e.g., Lenny faces and hashtags) or unmasking profanities. The text cleaning functions and regex expressions can be found [here](https://github.com/ZILiAT-NASK/BAN-PL/tree/main/src/utils.py).

## Disclaimer
It is important to acknowledge that certain comments featured within this dataset might have originally been part of a multi-modal content, involving not only textual elements but also accompanying images or videos. The absence of these supplementary modalities could potentially result in a misinterpretation of the initially prohibited textual content. We are dedicated to thorough data refinement efforts aimed at minimizing such instances.

Furthermore, we wish to highlight that, despite our meticulous manual annotation and verification processes, the anonymization procedure employed might not have achieved complete effectiveness. Some degree of errors or inaccuracies may persist despite our best efforts.

## Licence
The dataset and code in the repository are made available under a Creative Commons Attribution International 4.0 licence [(CC BY)](https://creativecommons.org/licenses/by/4.0/).

## Contact
Please contact the [Department of Linguistic Engineering and Text Analysis](mailto:ziliat@nask.pl?subject=[GitHub]%20BAN-PL%20Dataset) in case of any issues with the datasets.

## Citation
If you make use of this dataset, please cite the following paper.

Kołos, A., Okulska, I., Głąbińska, K., Karlińska, A., Wiśnios, E., Ellerik, P., Prałat, A. [*BAN-PL: a Novel Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service*](https://arxiv.org/abs/2308.10592). 2023. arXiv:2308.1059.

```
@misc{kołos2024banpl,
      title={BAN-PL: a Novel Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service}, 
      author={Anna Kołos and Inez Okulska and Kinga Głąbińska and Agnieszka Karlińska and Emilia Wiśnios and Paweł Ellerik and Andrzej Prałat},
      year={2024},
      eprint={2308.10592},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Acknowledgment
The work was carried out within the KOMTUR project ("System for categorising, evaluating, and moderating online content for new services and advertising selection"), which was funded by the National Centre for Research and Development in Poland within the 3/1.1.1/2020 Operational Programme Smart Growth 2014–2020, co-financed with the European Regional Development Fund. 
The authors would like to thank the team from Wykop.pl, especially Paweł Ellerik and Andrzej Prałat, engaged in the project for cooperating on the corpus and patiently answering all the endless related questions as well as helping in the data collection.





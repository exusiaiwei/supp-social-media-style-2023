# Undergraduate Graduation Project Attachment

[中文版](https://github.com/exusiaiwei/undergraduate-graduation-project-attachment/blob/main/readme.zh-CN.md)

![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)

![GitHub Repo stars](https://img.shields.io/github/stars/exusiaiwei/undergraduate-graduation-project-attachment)

![GitHub forks](https://img.shields.io/github/forks/exusiaiwei/undergraduate-graduation-project-attachment)

This project contains the attachment materials for my undergraduate graduation project. It includes the corpus and the code for corpus processing and data analysis.

## Table of Contents

- [Undergraduate Graduation Project Attachment](#undergraduate-graduation-project-attachment)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Installation](#installation)
  - [Instructions](#instructions)
    - [Corpus Overview](#corpus-overview)
    - [Topics and Domains Included in the Corpus](#topics-and-domains-included-in-the-corpus)
    - [Corpus Sources](#corpus-sources)
    - [Corpus Cleaning and Preprocessing](#corpus-cleaning-and-preprocessing)
  - [Badges](#badges)
  - [Related Repositories](#related-repositories)
  - [Maintainers](#maintainers)
  - [License](#license)

## Background

This is the attachment materials for my undergraduate graduation project.

## Installation

Download the project using Git and make edits and modifications locally.

The related code needs to be modified with the file paths before running.

## Instructions

The Corpus folder contains the self-built corpora.

The Code folder contains the code for corpus cleaning and data analysis, including Python and R code.

### Corpus Overview
This study constructs a self-built web corpus, mainly used for controlling topics and platforms. This corpus focuses on the following aspects of data:

- **Platform Selection**: Bilibili, Tieba, Weibo, and other popular platforms are selected. These platforms have a large number of users and cover multiple thematic areas.
- **Topic Classification**: Based on the classification of politics, literature, technology, and affairs, this study selects six domains: Film, Gaming, Learning, Literature, Politics, and Technology. A total of 18 typical keywords are included.

The corpus is stored in txt format, with the naming format as "Topic-Form-Source Platform".

### Topics and Domains Included in the Corpus

| Domain | Topic (Keywords) | Domain | Topic (Keywords) |
|--------|-----------------|--------|-----------------|
| Film   | The Wandering Earth | Technology | Artificial Intelligence (AI) |
|        | Man Jiang Hong |          | ChatGPT |
|        | Yi Yang Qian Xi | Literature | Dao Gui Yi Xian |
|        |                 |          | Keigo Higashino |
|        |                 |          | The Three-Body Problem |
|        |                 | Politics | Bride Price |
| Gaming | Arknights |             | Ohio |
|        | Girls' Frontline |       | Russo-Ukrainian War |
|        | StarCraft II |          | Population |
|        | Stellaris |             | Pandemic |
|        | Genshin Impact |         | Aircraft Carrier |

- Total Corpus Size: 61.2MB
- Total Word Count: Approximately 21 million words

### Corpus Sources
The corpora used in this study were collected from public platforms using open-source web crawlers or software. The specific methods are as follows:

- **Weibo Corpus**: Collected using the open-source project `WeiboSpider-master`.
- **Tieba Corpus**: Collected using the open-source project `Tieba_Spider-master` with some modifications and configurations.
- **Bilibili Corpus**: Collected using the data scraping software `Octopus Collector`, mainly focusing on the comments below the videos.

### Corpus Cleaning and Preprocessing
Due to the differences in crawling tools and platform characteristics, we performed necessary cleaning and preprocessing on the corpus to ensure data consistency and accuracy. The specific operations include:

- **Link Removal**: Using a Python program to batch remove image links and emoticon links from the corpus.
- **Word Segmentation**: For Chinese corpora, we used the `NLPIR-Parser` software for new word extraction and word segmentation.

The above is a detailed introduction to the corpora used in this study. Feel free to view and use this data on GitHub.

## Badges

![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)

![GitHub Repo stars](https://img.shields.io/github/stars/exusiaiwei/undergraduate-graduation-project-attachment)

![GitHub forks](https://img.shields.io/github/forks/exusiaiwei/undergraduate-graduation-project-attachment)

## Related Repositories

[Tieba_Spider](https://github.com/Aqua-Dream/Tieba_Spider) - I made some modifications to this archived project for collecting data for my thesis.

[WeiboSpider](https://github.com/nghuyong/WeiboSpider) - I used this project for collecting data for my thesis.

## Maintainers

@exusiaiwei

## License

[MIT](LICENSE) © exusiaiwei

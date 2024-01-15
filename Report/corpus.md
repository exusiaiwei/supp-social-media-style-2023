
### Corpus Overview
The corpus constructed in this study is a self-built web corpus, primarily used for controlling topics and platforms. This corpus focuses on the following aspects of data:

- **Platform Selection**: Bilibili, Tieba, and Weibo were chosen as popular platforms, as they have a large user base and cover multiple thematic domains.
- **Topic Classification**: Based on the classification of politics, literature, technology, and affairs, this study selected six domains: Film, Gaming, Learning, Literature, Politics, and Technology. It includes a total of 18 typical keywords.

### Topics and Domains Included in the Corpus

| Domain | Topic (Keywords) | Domain | Topic (Keywords) |
|--------|-----------------|--------|-----------------|
| Film   | The Wandering Earth | Technology | Artificial Intelligence (AI) |
|        | Man Jiang Hong |        | ChatGPT |
|        | Yi Yangqianxi | Literature | Dao Gui Yi Xian |
|        |                 |        | Keigo Higashino |
|        |                 |        | The Three-Body Problem |
|        |                 | Politics | Dowry |
| Gaming | Arknights |        | Ohio |
|        | Girls' Frontline |        | Russo-Ukrainian War |
|        | StarCraft II |        | Population |
|        | Stellaris |        | Epidemic |
|        | Genshin Impact |        | Aircraft Carrier |

- Total Corpus Size: 61.2MB
- Total Word Count: Approximately 21 million words

### Corpus Source
The corpora used in this study were collected from public platforms using open-source web crawlers or software. The specific methods are as follows:

- **Weibo Corpus**: Collected using the open-source project `WeiboSpider-master`.
- **Tieba Corpus**: Collected using the open-source project `Tieba_Spider-master`, with some modifications and configurations.
- **Bilibili Corpus**: Collected using the data scraping software `Octopus Collector`, mainly focusing on the comments below videos.

### Corpus Cleaning and Preprocessing
Due to the different crawling tools and platform characteristics, we performed necessary cleaning and preprocessing on the corpora to ensure consistency and accuracy of the data. The specific operations include:

- **Link Removal**: Batch removal of image links and emoticon links from the corpora using Python scripts.
- **Word Segmentation**: For Chinese corpora, we used the `NLPIR-Parser` software for new word extraction and word segmentation.

The above provides a detailed introduction to the corpora used in this study. Feel free to view and use this data on GitHub.

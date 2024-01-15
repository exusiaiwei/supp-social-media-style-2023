# 本科毕业设计附属材料

[English version](https://github.com/exusiaiwei/undergraduate-graduation-project-attachment/blob/main/readme.md)

![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)

![GitHub Repo stars](https://img.shields.io/github/stars/exusiaiwei/undergraduate-graduation-project-attachment)

![GitHub forks](https://img.shields.io/github/forks/exusiaiwei/undergraduate-graduation-project-attachment)
本项目为本科毕业设计附属材料。包括语料库和进行语料处理，数据分析的代码。

## 内容列表

- [本科毕业设计附属材料](#本科毕业设计附属材料)
  - [内容列表](#内容列表)
  - [背景](#背景)
  - [安装](#安装)
  - [使用说明](#使用说明)
    - [语料库概述](#语料库概述)
    - [语料库所包含的主题和领域](#语料库所包含的主题和领域)
    - [语料来源](#语料来源)
    - [语料清洗和预处理](#语料清洗和预处理)
  - [徽章](#徽章)
  - [相关仓库](#相关仓库)
  - [维护者](#维护者)
  - [使用许可](#使用许可)

## 背景

这是我本科毕业设计的附属材料。

## 安装

使用Git下载到本地进行编辑和修改。

相关代码需要修改文件地址之后运行。

## 使用说明

Corpus文件夹中是自建的语料库。

Code文件夹中是用于语料清洗和数据分析的代码，包括Python和R代码。

###  语料库概述
本研究构建的是一个自建的网络语料库，主要用于控制主题和平台。本语料库着重于以下几个方面的数据：

- **平台选择**：选择了B站、贴吧、微博这些大众平台，这些平台使用人数众多，且涵盖多个主题领域。
- **主题分类**：基于政论、文艺、科技、事务的分类法，本研究选择了Film,Gaming,Learning,Literature,Politics,Technology六个领域。总共包含18个典型关键词。

语料以txt格式存储，命名格式为“主题-形式-来源平台”。

###  语料库所包含的主题和领域

| 领域 | 主题（关键词） | 领域 | 主题（关键词） |
|------|----------------|------|----------------|
| 影视 | 流浪地球       | 科技 | 人工智能（ai） |
|      | 满江红         |      | chatgpt        |
|      | 易烊千玺       | 文学 | 道诡异仙       |
|      |                |      | 东野圭吾       |
|      |                |      | 三体           |
|      |                | 政治 | 彩礼           |
| 游戏 | 明日方舟       |      | 俄亥俄         |
|      | 少女前线       |      | 俄乌战争       |
|      | 星际争霸2      |      | 人口           |
|      | 星穹铁道       |      | 疫情           |
|      | 原神           |      | 航空母舰       |

- 语料库总量：61.2MB
- 总字数：约2100万字

### 语料来源
本研究使用的语料均通过开源爬虫项目或软件从公开平台爬取。具体方法如下：

- **微博语料**：使用开源项目`WeiboSpider-master`进行搜集。
- **贴吧语料**：使用开源项目`Tieba_Spider-master`进行搜集，并进行了一定的修改和配置。
- **B站语料**：使用数据抓取软件`八爪鱼采集器`进行搜集，主要针对视频下方的评论信息。

### 语料清洗和预处理
由于不同的抓取工具和平台特性，我们对语料进行了必要的清洗和预处理，以确保数据的一致性和准确性。具体操作包括：

- **链接移除**：使用Python程序批量删除了语料中的图片链接和表情符号链接。
- **分词处理**：针对中文语料的特点，使用`NLPIR-Parser`软件进行了新词提取和分词处理。

以上是对本研究中使用的语料库的详细介绍。欢迎在GitHub上查看和使用这些数据。


## 徽章

![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)

![GitHub Repo stars](https://img.shields.io/github/stars/exusiaiwei/undergraduate-graduation-project-attachment)

![GitHub forks](https://img.shields.io/github/forks/exusiaiwei/undergraduate-graduation-project-attachment)
## 相关仓库

[Tieba_Spider](https://github.com/Aqua-Dream/Tieba_Spider) - 我在这个已经存档的项目上进行了一些修改，以进行论文数据的抓取。

[WeiboSpider](https://github.com/nghuyong/WeiboSpider) - 我使用这个项目进行论文数据抓取。

## 维护者

@exusiaiwei

## 使用许可

[MIT](LICENSE) © exusiaiwei

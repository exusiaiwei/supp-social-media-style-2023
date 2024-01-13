# 读取excel表格，假设文件名为data.xlsx
library(readxl)
data <- read_excel("data.xlsx")

# 将领域和平台变量转换为因子类型
data$领域 <- as.factor(data$领域)
data$平台 <- as.factor(data$平台)

# 进行单变量方差分析，假设h点服从正态分布
model <- aov(h点 ~ 领域 + 平台, data = data)

# 查看方差分析结果
summary(model)

# 进行多重比较，使用Tukey方法
library(multcomp)
tukey <- glht(model, linfct = mcp(领域 = "Tukey", 平台 = "Tukey"))

# 查看多重比较结果
summary(tukey)

# 进行可视化，使用ggplot2包
library(ggplot2)

# 绘制h点与领域的箱线图
ggplot(data, aes(x = 领域, y = h点)) +
  geom_boxplot() +
  labs(title = "h点与领域的关系", x = "领域", y = "h点")

# 绘制h点与平台的箱线图
ggplot(data, aes(x = 平台, y = h点)) +
  geom_boxplot() +
  labs(title = "h点与平台的关系", x = "平台", y = "h点")
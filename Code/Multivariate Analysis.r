# 安装readxl和car包
install.packages("readxl")
install.packages("car")

# 加载包
library(readxl)
library(car)

# 读取Excel表格
my_data <- read_excel("C:/Research/Analyse/analyse.xlsx")
df[,1:3] <- lapply(df[,1:3], as.factor)

# 进行多因素方差分析
fit <- aov(Tokens ~ 主题 + 体裁 + 平台, data = my_data)

# 显示方差分析结果
summary(fit)

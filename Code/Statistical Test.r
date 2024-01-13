# 读取Excel表格
library(readxl)
data <- read_excel("C:/Research/Analyse/analyse.xlsx")

# 将第四列和第五列转换为数值类型
data[, 4] <- as.numeric(data[, 4])
data[, 5] <- as.numeric(data[, 5])

# 进行正态性检验
h点_shapiro <- shapiro.test(data[, 4])
entropy_shapiro <- shapiro.test(data[, 5])

# 进行方差齐性检验
library(car)
h点_bartlett <- bartlett.test(data[, 4] ~ data[, 3])
entropy_levene <- leveneTest(data[, 5] ~ data[, 3])

# 输出检验结果
print(h点_shapiro)
print(entropy_shapiro)
print(h点_bartlett)
print(entropy_levene)
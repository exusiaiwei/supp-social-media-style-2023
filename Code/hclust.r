#install.packages("readxl")
#install.packages("dplyr")
#install.packages("ggplot2")

library(readxl)
library(dplyr)
library(ggplot2)

data <- read_excel("")

selected_cols <- c(1,2,3,4:ncol(data))
selected_data <- data[, selected_cols]

distance_matrix <- dist(selected_data[,4:ncol(selected_data)])
clustering_result <- hclust(distance_matrix)

plot(clustering_result, hang=-1, main="聚类结果", xlab="", sub="", ylab="")

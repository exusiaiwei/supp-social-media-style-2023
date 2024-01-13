# 导入readxl和cluster库
library(readxl)
library(cluster)

# 读取Excel文件数据
data <- read_excel("")


# 遍历每个分类依据
for (i in 1:3) {
  # 获取分类依据的列名
  cat_col <- names(data)[i]
  
  # 遍历每两个数据指标
  for (j in 4:(ncol(data) - 1)) {
    for (k in (j+1):ncol(data)) {
      # 获取数据指标的列名
      data_col1 <- names(data)[j]
      data_col2 <- names(data)[k]
      
      # 构建数据子集
      subset_data <- data[, c(i, j, k)]
      
      # 计算距离矩阵
      d <- dist(subset_data[, -1], method = "euclidean")
      
      # 使用PAM算法聚类
      pam_fit <- pam(d, k = 3, diss = TRUE)
      
      # 绘制聚类图
      png(file = paste0("clusplot_", cat_col, "_", data_col1, "_", data_col2, ".png"), width = 800, height = 800)
      clusplot(subset_data[, -1], pam_fit$clustering,
               main = paste("PAM聚类结果 - Category ", i,
                            " - Columns ", data_col1, " & ", data_col2),
               color = TRUE, shade = TRUE, labels = 2, lines = 0)
      dev.off()
      
      # 绘制轮廓显影图
      library(cluster)
      sil_width <- silhouette(pam_fit$clustering, d)
      png(file = paste0("silhouette_", cat_col, "_", data_col1, "_", data_col2, ".png"), width = 800, height = 800)
      plot(sil_width, main = paste("轮廓显影图 - Category ", i,
                                   " - Columns ", data_col1, " & ", data_col2))
      dev.off()
    }
  }
}


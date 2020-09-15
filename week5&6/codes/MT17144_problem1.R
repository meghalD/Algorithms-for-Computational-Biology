#Q1
data <- read.table("C:\\Users\\MeghalD\\Downloads\\count_brain.txt",sep=",",stringsAsFactors=F,header=T)
library(edgeR)
TMM <- calcNormFactors(as.matrix(data),method="TMM")
norm_data <- (data)/((TMM)*colSums(data))
trans_data <- log2(norm_data+1)

#kmeans
k_means <- kmeans(trans_data,5,nstart=20)
pca <- prcomp(trans_data)
plot(pca$x[,1],pca$x[,2],col=k_means$cluster, pch=16)

#fuzzy
library(cluster)
p = princomp(na.omit(trans_data))

loadings = p$loadings[]

x = loadings[,1]
y = loadings[,2]
f_clust <- fanny(cbind(x,y), 5, metric = "euclidean", stand = FALSE, maxit = 500)
plot(f_clust)


#Diff exp analysis
library(DESeq2)
data_clean <- data[1:(nrow(data) - 5), ]
cpm_log <- cpm(data_clean, log = TRUE)
heatmap(cor(cpm_log))


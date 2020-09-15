#Q2
data <- read.table("C:\\Users\\MeghalD\\Downloads\\counts_gene.tsv",stringsAsFactors=F,header=T)
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


#plot(pca1$x[,1],pca1$x[,2],col=f_clust$cluster, pch=16)

library(dbscan)
#library("fpc")
#set.seed(123)
db <- dbscan(cbind(x,y), eps = 15, MinPts = 20)
# Plot DBSCAN results
hullplot(cbind(x,y),db$cluster)


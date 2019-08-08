gene<-read.table("novellncRNA_pheatmap.txt",header=TRUE,sep="\t")
library(pheatmap)
gene2<-gene[,2:3]
#rownames(data)<-paste("Gene", 1:80, sep = "")
rownames(gene2)<-gene$gene
annotation_row = data.frame(GeneClass = factor(rep(c("sense_intronic","processed_tramscript","sense_overlapping","lincRNA","antisense"), c(3,47,5,1,1))))
#rownames(annotation_row) = paste("Gene", 1:80, sep = "")
rownames(annotation_row)<-gene$gene
ann_colors = list(CellType = c(CT1 = "ZIKV", CT2 = "Control"))
pheatmap(gene2,color = colorRampPalette(c("blue", "orange", "red"))(57),cluster_cols=FALSE,show_rownames =TRUE,annotation_row = annotation_row,cluster_rows=FALSE,annotation_colors = ann_colors,cellwidth=50)

gene<-read.table("annotatedlncRNA_pheatmap.txt",header=TRUE,sep="\t")
library(pheatmap)
gene2<-gene[,2:3]
#rownames(data)<-paste("Gene", 1:80, sep = "")
rownames(gene2)<-gene$gene
annotation_row = data.frame(GeneClass = factor(rep(c("antisense","lincRNA","processed_tramscript","sense_intronic"), c(31,45,14,2))))
#rownames(annotation_row) = paste("Gene", 1:80, sep = "")
rownames(annotation_row)<-gene$gene
ann_colors = list(CellType = c(CT1 = "ZIKV", CT2 = "Control"))
pheatmap(gene2,color = colorRampPalette(c("blue", "orange", "red"))(92),cluster_cols=FALSE,show_rownames =TRUE,annotation_row = annotation_row,cluster_rows=FALSE,annotation_colors = ann_colors,cellwidth=50)
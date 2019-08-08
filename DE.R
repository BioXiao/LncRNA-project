gene<-read.table("paired.txt",header=T,sep="\t")
plot(gene$Control,gene$Zika,col=as.character(gene$Col),pch=20, bty = "n",las=1,cex.axis=1.2)
legend("topright",col=c("red","blue","gray"),c("Significant-Up","Significant-Down","Nonsignificant"),pch=20)

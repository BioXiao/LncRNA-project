gene<-read.table("novel_sigdiff.txt",header=TRUE,sep="\t")
plot(log10(gene$control),log10(gene$zikv),col=as.character(gene$col),xlab="Gene Expression Level of Control",ylab="Gene Expression Level of ZIKV  Infection",main="RNA-seq Gene Differential Expression",pch=20,bty="n",las=1,ylim=c(-0.5,2.0))
legend("bottomright",col=c("red","blue"),c("Significant-Up","Significant-Down"),pch=20)
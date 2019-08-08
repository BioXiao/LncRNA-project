ddf = data.frame(NUMS = rnorm(500), GRP = sample(LETTERS[1:5],500,replace=T))
boxplot(NUMS ~ GRP, data = ddf, lwd = 2, ylab = 'NUMS')
stripchart(NUMS ~ GRP, vertical = TRUE, data = ddf,method = "jitter", add = TRUE, pch = 20, col = 'blue')


boxplot(log10(box),notch=TRUE,col=c("CornflowerBlue","DarkSeaGreen2","Pink2"),outline=FALSE,ylim=c(-4,4))
stripchart(log10(box),vertical = TRUE,method = "jitter", add = TRUE, pch = 20, col = 'blue')


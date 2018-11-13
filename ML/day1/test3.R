#/home/ai20/Desktop/common/ML/Day1/Questions

library(caret)
library(e1071)
dataset1 <- read.table(file.choose())
dataset <- dataset1[,-1]
fit.knn <-train(V9~.,data = dataset,method = 'knn')
predict(fit.knn,dataset[1,(1:8)])

#v <- createDataPartition(dataset$V9,p=0.8,list=FALSE)
#trainData <- dataset[v,]
#testData <- dataset[-v,]
#fit.knn <-train(V9~.,data = trainData,method = 'knn')
#predictions <- predict(fit.knn,testData)


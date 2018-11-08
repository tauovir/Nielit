#====First Question========
library(caret)
library(e1071)
dataset <- iris
head(dataset)
#?head()
dataset$Species
v <- createDataPartition(dataset$Species,p=0.8,list=FALSE)
trainData <- dataset[v,]
testData <- dataset[-v,]

fit.knn <-train(Species~.,data = trainData,method = 'knn')
#predict(fit.knn,dataset[1,(1:4)])
predictions <- predict(fit.knn,testData)
confusionMatrix(testData[,5],predictions)







#==========First Question========
library(caret)
library(e1071)
dataset <- iris
head(dataset)
#?head()
dataset$Species
fit.knn <-train(Species~.,data = dataset,method = 'knn')
predict(fit.knn,dataset[1,(1:4)])







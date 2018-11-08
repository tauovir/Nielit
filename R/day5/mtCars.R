mtcars= dataset
#mtcars
newData = data.frame(mpg=mtcars$mpg,cyl=mtcars$cyl,hp=mtcars$hp)
newData
headData <- head(newData,5)
tailData <- tail(newData,5)
cData <- rbind(headData, tailData)
cData

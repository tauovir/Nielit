#Draw a pie-chart for moview review
user <- sample(1:20,4)
user
movieType <- c("Comedy",'Action','Romance','Science Fiction')
movieType
colorX <- c("Red","blue","green","black")
colorX
pie(user,movieType,radius = 1,main = "Movie",col=colorX,clockwise=TRUE)
legend("topleft",movieType,fill=colorX)

?pie
?legend


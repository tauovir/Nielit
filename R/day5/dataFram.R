xm <- data.frame(age=c(25,31,23),
    hiight=c(177,163,190),
    weight = c(57,69,83),
    gender=c("F","F","M"))
row.names(xm)= c("Alex","Lilly","Mark")
xm
#Now Create second Data frame
xm2 <- data.frame(working = c("Yes","No","No"))
xm2
row.names(xm2) = c("Alex","Lilly","Mark")
xm2
#Now Add data fram
rs<-cbind(xm,xm2)
rs
#N0ow Find data type of each column
class(rs$age)#Age is numeric type
class(rs$hiight)#Height is numeric type
class(rs$weight)#Weight is numeric type
class(rs$gender)#Gender is Factor type
class(rs$working)#Working is Factor type

#Find Bmi of all and add it to new column
bmi <- rs$weight / ((rs$hiight)/100)^2
bmi
rs <- cbind(rs,bmi)
rs
#Now Find Heathy Person
health <- bmi < 25
rs <- cbind(rs,health)
rs
#Now Read Data from File
getwd()
#/home/ai20/Desktop/common/R/Day4/Data
r1 <- read.table(file.choose())
r1
r2 <- read.table(file.choose())
r2



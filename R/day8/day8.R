#==========Question 1==========
x1 <- dbinom(5,50,0.8)
x2 <- dbinom(5,50,0.5)
x3 <- pbinom(5,50,0.8)
x5 <- pbinom(25,50,0.8)
x6 <- pbinom(5,50,0.5)
#=========Question 2========
y1 <-  dbinom(40,60,0.65)
y2 <-  pbinom(40,60,0.65)
#============Third Question========
x <- seq(0,30,1)
y1 <- dbinom(sq1,30,0.5)
plot(x,y1)
y2 <- dbinom(sq1,30,0.4)
plot(x,y2)
y3 <- dbinom(sq1,30,0.8)
plot(x,y3)
#===========Question Fourth=========
comb <- c(20,25,30)
p1 <- pbinom(comb,60,0.5)
p2 <- pbinom(20,60,0.5)
bt <- c(21:29)
p2 <- pbinom(bt,60,0.5)
#=========Sixth Question=======
 xx = rpois(2608,lambda = 10097/2608)
hist(xx)
#=========Seventh Question=======
m1 = ppois(5,lambda = 7)
m2 = ppois(10,lambda = 7)
cc <- c(5:15)
m3 = ppois(cc,lambda = 7)
#========8th Question============
x <-punif(6,0,25)
#=============5th Question========
df <- c(1:20)
mn <- mean(df)
rs <- ppois(100,lambda = mn)


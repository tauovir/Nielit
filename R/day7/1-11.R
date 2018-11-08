s1 <- sample(c(1:6),300,replace = TRUE)
s2 <- sample(c(30:70),27,replace = TRUE)
s3 <- sample(c(1:2),100,replace = TRUE)
?sample
s1
s2
s3
#Second Question
k <- rnorm(100,0,30)
k
round(k,0)
prob <- dnorm(k,0,30)
prob
plot(k,prob)
#cumulative distribution points
cum <- pnorm(k,0,30)
plot(k,cum)
#question 2.c
qn <- qnorm(0.2,0,30)
#Question 2.d
qn1 <- qnorm(0.5,0,30)

#==============Question 3==============
k1 <- rnorm(100,0,30)
k1
round(k1,0)
prob <- dnorm(k1,0,30)
prob
plot(k1,prob)

#=================Draw Histogram==========
h <- rnorm(100,20,5)
hist(h)
#==========Question 5========
mean1 <- c(22)
varience <- c(25)
sd <- sqrt(varience)
a <- (1 - pnorm(29,mean1,sd))
a1 <-  pnorm(17,mean1,sd)
a1
a2 <-  pnorm(15,mean1,sd) + (1 - pnorm(25,mean1,sd))
a2
#=======sixth Question=======
mean1 <- c(30)
var <- c(4)
sd1 <- sqrt(var)
fg <- 1/(sqrt(2*pi)*sd1)*exp(-((31 - mean1)^2/(2*sd1^2)))
#Varify it with Dnorm
zz <- dnorm(31,mean1,sd1)










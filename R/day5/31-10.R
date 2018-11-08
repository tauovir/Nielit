age <- c(2,3,5,7,8)
w <- c(14,20,32,42,44)
r <- lm(w~age)
k<-data.frame(age=6)
predict(r,k)
plot(age,w)
abline(r)
#Linear Corelation coffecient
x <- c(8,7,6,4,2,1)
y <- c(15,19,25,23,34,40)
cor(x,y)
r1 <- lm(x~y)
k1<-data.frame(y=2)
predict(r1,k1)

r2 <- lm(y~x)
k2<-data.frame(x=5)
predict(r2,k2)
#Grade
h <- c(186,189,190,192,193,193,198,201,203,205)
w <-c (85,85,86,90,87,91,93,103,100,101)
rr1 <- lm (w~h)
plot(w,h)
abline(rr1,col="red")
cor(h,w)
kk<-data.frame(h=208)
predict(rr1,kk)

#Hours and corelation
hr <- c(80,79,83,84,78,60,82,85,79,84,80,62)
pr <- c(300,302,315,330,300,250,300,340,315,330,310,240)
regg = lm(hr~pr)
plot(hr,pr)
abline(regg)
cor(hr,pr)

#Sleeping
sr <- c(6,7,8,9,10)
tl <- c(4,3,3,2,1)
cor(sr,tl)
regr = lm (sr~tl)
regr1 = lm (tl~sr)
plot(sr,tl)
abline(regr)
z <- data.frame(sr=8)
predict(regr1,z)
#Last
x1 <- c(25,42,33,54,29,36)
y1 <- c(42,72,50,90,45,48)
cor(x1,y1)
g1 <- lm(y1~x1)
plot(x1,y1)
abline(g1)
kk1 <- data.frame(x1 = 47)
predict(g1,kk1)






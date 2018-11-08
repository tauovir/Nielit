mat <- matrix(c(10,20,31,25,26,28,17,1,45,14,27,26),nrow=3,ncol=4)
mat
product <- c("RedMe",'Apple','IPhone')
product
colorX <- c("Red","blue","green")
  barplot(mat,
        xlab="Quarter",
        ylab="Sold Product",
        main = "Company Sales Data",
        col = colorX
  )

 
legend("topleft",product,fill=colorX)

?legend
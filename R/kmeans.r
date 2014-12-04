

#iris_file <- "/home/martin/Dev/DataMining/data/iris.csv"
#d <- read.csv(iris_file,header=FALSE)[0:4]
spat_file <- "/home/martin/Dev/DataMining/data/3D_spatial_network.txt"
d <- read.csv(spat_file,header=FALSE)
k <- 3


options(max.print=20)

for (i in 1:100) {
    cat("round")
    print(i)
    print( system.time(result <- kmeans(d,k)))

    cat("iterations")
    print(result$iter)
    cat("totalcost")
    print(result$totss)
}


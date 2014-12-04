
using DataFrames
using Clustering


#raw_data = readtable("/home/martin/Dev/DataMining/data/iris.csv", header=false)[:,[1:4]]
raw_data = readtable("/home/martin/Dev/DataMining/data/3D_spatial_network.txt", header=false, eltypes=[Float64,Float64,Float64,Float64])

matrix = transpose(array(raw_data))

k = 3

for i = 1:100
    print("new round ")
    println(i)

    #@time measuring
    @time result = kmeans(matrix, k)
    #@time result = kmeans(matrix,k;init=:kmpp)
    print("totalcost ")
    println(result.totalcost)
    print("iterations ")
    println(result.iterations)
    print("converged ")
    println(result.converged)
end


println("test run done")



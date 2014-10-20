
using DataFrames
using Clustering


iris = readtable("/home/martin/Dev/DataMining/data/iris.csv", header=false)[:,[1:4]]

iris_matrix = transpose(array(iris))

result = kmeans(iris_matrix, 3)

print(result.counts)
print(result.assignments)

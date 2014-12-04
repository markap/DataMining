#!/bin/bash

# piping of ouput
# ./kmeans.sh > kmeans.result 2>&1

WEKA=/home/martin/apps/weka-3-6-11/weka.jar
K=3

#ARFF_FILE=/home/martin/Dev/DataMining/data/iris15K.csv.arff
ARFF_FILE=/home/martin/Dev/DataMining/data/3D_spatial_network.arff


for i in `seq 1 100`;
do
    echo "new round $i"
    time java -Xmx8g -cp $WEKA weka.clusterers.SimpleKMeans -N $K -A "weka.core.EuclideanDistance -R first-last" -I 500 -S 10 -t $ARFF_FILE
done

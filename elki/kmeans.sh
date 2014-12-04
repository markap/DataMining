#!/bin/bash

ELKI=/home/martin/apps/elki/elki.jar
K=3


#FILE=/home/martin/Dev/DataMining/data/iris.csv
FILE=/home/martin/Dev/DataMining/data/3D_spatial_network.txt

#ALGORITHM=clustering.kmeans.KMeansLloyd
ALGORITHM=clustering.kmeans.ParallelLloydKMeans



for i in `seq 1 25`;
do
    echo "new round $i"
    # @todo drop 5th column for iris
    time java -jar $ELKI KDDCLIApplication -dbc.in $FILE -algorithm $ALGORITHM -kmeans.k $K -resulthandler DiscardResultHandler

done

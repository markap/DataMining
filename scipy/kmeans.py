import timeit
import numpy as np
#from scipy.cluster.vq import kmeans
from scipy.cluster.vq import kmeans2


#filename = "/home/martin/Dev/DataMining/data/iris15K.csv"
filename = "/home/martin/Dev/DataMining/data/3D_spatial_network.txt"


d = np.genfromtxt(filename, delimiter=',')[:,0:4]
k = 3


def do_time():
    t = timeit.Timer("kmeans2(d,k)")
    time = t.timeit(1)
    print "time elapsed %f \n" % time

import __builtin__
__builtin__.__dict__.update(locals())


for i in range(0,100):
    print "next round %d \n" % i
    do_time()


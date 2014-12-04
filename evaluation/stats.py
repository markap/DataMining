
def compute_stats(df):


    print "mean time is "
    print df.time.mean()
    print "max 10 times"
    print df.sort('time', ascending=False).head(10)
    print "min 10 times"
    print df.sort('time', ascending=True).head(10)
    print


    print "all converged?"
    print df.groupby('converged').agg('count')
    print

    print "total cost group by"
    print df.groupby('totalcost').agg('count')
    print "total cost mean"
    print df.totalcost.mean()
    print 

    print "iterations group by"
    print df.groupby('iterations').agg('count')
    print "avg iterations"
    print df.iterations.mean()




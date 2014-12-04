from optparse import OptionParser
import stats
import pandas as pd

def parse_result_file(filename):
    result = []
    with open(filename) as f:
        data ={}
        for line in f:

            if "new round" in line:
                data['round'] = get_round(line)
            elif "elapsed time" in line:
                data['time'] = get_time(line)
            elif "iterations" in line:
                data['iterations'] = get_iterations(line)
            elif "totalcost" in line:
                data['totalcost'] = get_totalcost(line)
            elif "converged" in line:
                data['converged'] = get_converged(line)
                result.append(data)
                data = {}

    f.close()

    df = pd.DataFrame(result)
    stats.compute_stats(df.ix[1:])


 
def get_round(line):
    return int(line.split()[2])

def get_time(line):
    return float(line.split()[2])

def get_totalcost(line):
    return float(line.split()[1])

def get_iterations(line):
    return int(line.split()[1])

def get_converged(line):
    return bool(line.split()[1])
        


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="the file to parse", metavar="FILE")


(options, args) = parser.parse_args()

parse_result_file(options.filename)



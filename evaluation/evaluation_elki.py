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
            elif "real" in line:
                data['time'] = get_time(line)
                data['converged'] = True
                data['iterations'] = 0
                data['totalcost'] = 0
                result.append(data)
                data = {}

    f.close()

    df = pd.DataFrame(result)

    stats.compute_stats(df)


 
def get_round(line):
    return int(line.split()[2])

def get_time(line):
    timeStr = line.split()[1]
    return float(timeStr.split('m')[1][:-1])

def get_totalcost(line):
    return float(line.split()[6])

def get_iterations(line):
    return int(line.split()[3])

def get_converged(line):
    return bool(line.split()[1])
        


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="the file to parse", metavar="FILE")


(options, args) = parser.parse_args()

parse_result_file(options.filename)



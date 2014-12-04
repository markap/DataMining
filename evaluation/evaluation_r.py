from optparse import OptionParser
import stats
import pandas as pd

def parse_result_file(filename):
    result = []
    with open(filename) as f:
        data ={}
        timeInNextLine = False

        for line in f:

            if "round" in line:
                data['round'] = get_round(line)
            elif "elapsed" in line:
                timeInNextLine = True
            elif "iterations" in line:
                data['iterations'] = get_iterations(line)
            elif "totalcost" in line:
                data['totalcost'] = get_totalcost(line)
                data['converged'] = True
                result.append(data)
                data = {}
            elif timeInNextLine:
                timeInNextLine = False
                data['time'] = get_time(line)

    f.close()

    df = pd.DataFrame(result)
    stats.compute_stats(df)


 
def get_round(line):
    return int(line.split()[1])

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



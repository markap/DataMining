from optparse import OptionParser
import stats
import pandas as pd

def parse_result_file(filename):
    result = []
    with open(filename) as f:
        data ={}
        for line in f:

            if "next round" in line:
                data['round'] = get_round(line)
            elif "time elapsed" in line:
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
    return float(line.split()[2])



parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="the file to parse", metavar="FILE")


(options, args) = parser.parse_args()

parse_result_file(options.filename)



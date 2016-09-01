import pandas as pd
import matplotlib.pyplot as plt
import sys

file_name = sys.argv[1] if len(sys.argv) > 1 else 'output_8'

print "About to read {}".format(file_name)
data = pd.read_csv('outputs/{}.csv'.format(file_name))

data.columns = ['destination', 'deadline', 'did_reach']
data.drop('destination', axis=1, inplace=True)

print "Successful trips: {}".format(len(data[data['did_reach'] == True]))
print "Failed trips: {}".format(len(data[data['did_reach'] == False]))

# plt.figure()
#
# data.plot.hexbin(x='deadline', y='did_reach', gridsize=25)
#
# plt.savefig('visual_1.png')
# plt.show()

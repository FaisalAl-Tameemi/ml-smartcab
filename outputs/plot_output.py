import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('output.csv')

data.columns = ['destination', 'deadline', 'did_reach']
data.drop('destination', axis=1, inplace=True)

plt.figure()

data.plot.hexbin(x='deadline', y='did_reach', gridsize=25)

plt.savefig('visual_1.png')
# plt.show()

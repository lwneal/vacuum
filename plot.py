import sys
import numpy as np
import pandas as pd

# Hack to keep matplotlib from crashing when run without X
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Apply sane defaults to matplotlib
import seaborn as sns
sns.set_style('darkgrid')
print("Loaded seaborn style for Matplotlib")

if __name__ == '__main__':
    filename = sys.argv[1]
    df = pd.read_csv(filename)
    plot = df.plot(x='time', y='dirt')
    plot.set_title("Dirt over Time, {}".format(filename))
    plot.get_figure().savefig(filename.replace('.csv', '') + '.png')


import pandas as pd
import numpy as np
import sys

def get_output_fn(name):
    tokens = name.split('_')
    tokens = tokens[:-1]
    return 'averaged_{}.csv'.format('_'.join(tokens))

input_filenames = sys.argv[1:]
output_filename = get_output_fn(input_filenames[0])

dataframes = []
for filename in input_filenames:
    df = pd.read_csv(filename)
    dataframes.append(df)
new_df = sum(dataframes) / len(dataframes)
new_df.to_csv(output_filename)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def create_heatmap(df, col_name):
    x_axis_labels = [i for i in range(1, 32)]
    y_axis_labels = ['Sun', 'Sat', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon']  # labels for y-axis

    commerce_map = df[col_name].to_numpy()
    commerce_map = np.pad(commerce_map, (2, 2), 'constant')
    commerce_map = np.reshape(commerce_map, (31, 7))
    commerce_map = np.transpose(commerce_map)
    commerce_map = np.flip(commerce_map, axis=0)

    plt.figure(figsize=(10, 2.5))

    sns.set(font_scale=1.0)
    sns.heatmap(commerce_map, xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="YlGnBu")

    title_name = "Tweet Counts ({})".format(col_name)

    plt.title(title_name, fontsize=20)
    plt.xlabel('Week')
    #plt.show()
    plt.savefig('heatmap_state_{}.png'.format(col_name), dpi=300)
    plt.clf()


# Group By_date,commerce,Public,Residential,Nature,Industry,Recreation,Transport,Farmland,Others
# 1/1/2020 - 7/31/2020
df = pd.read_csv('total_merge_2_7.csv')
df.rename(columns={'commerce':'Commerce'}, inplace=True)

land_types = ['Commerce', 'Public', 'Residential', 'Nature', 'Industry', 'Recreation', 'Transport', 'Farmland', 'Others']
for land in land_types:
    create_heatmap(df, land)

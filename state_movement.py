import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def generate_graph(df, land_type):
    mylist = df[land_type].tolist()
    N = 7
    averages = []
    for i in range(N, len(mylist)+1, N):
        averages.append(sum(mylist[i-N:i]) / N)
    return averages


def grid(df):
    sns.set_style("white")
    g = sns.FacetGrid(df, col='county', hue='county', col_wrap=3, )
    g = g.map(plt.plot, 'Date', 'Geotweets-based Mobility Index (GMI)')
    g = g.map(plt.fill_between, 'Date', 'Geotweets-based Mobility Index (GMI)', alpha=0.2).set_titles("{col_name} country")
    g = g.set_titles("{col_name}", pad=-15)

    nums = [0, 4, 8, 12, 17, 21]
    counter = 0

    for ax in g.axes.flat:
        labels = ax.get_xticklabels()  # get x labels
        for i,l in enumerate(labels):
            if i not in nums: labels[i] = ''  # skip even labels
        ax.set_xticklabels(labels, rotation=90)  # set new labels

        vals = ax.get_yticks()

        ax.set_yticklabels(['-80%', '-60%', '-40%', '-20%', 'Baseline', '20%', '40%', '60%'])
        if counter % 3 == 0: ax.set_ylabel('Geotweets-based\nMobility Index (GMI)', fontsize=8.5)
        counter += 1

    for axis in g.axes: axis.set_xlabel('')

    plt.subplots_adjust(top=0.92)
    g = g.fig.suptitle('State Movement Changes')
    plt.subplots_adjust(left=0.15, bottom=0.07, right=0.82, top=0.92, wspace=0.12, hspace=0.28)

    plt.show()



df = pd.read_csv('04_medium_change_ratio_1_7.csv')

dates = ['Feb', 'Feb 14', 'Feb 21', 'Feb 28', 'Mar', 'Mar 13', 'Mar 20', 'Mar 27',
         'Apr', 'Apr 10', 'Apr 17', 'Apr 24', 'May', 'May 8', 'May 15', 'May 22',
         'May 29', 'Jun', 'Jun 12', 'Jun 19', 'Jun 26', 'Jul', 'Jul 10', 'Jul 17', 'Jul 24']
landtypes = ["Commercial", "Public", "Residential", "Nature", "Industry", "Recreation",
             "Transport", "Farmland", "Others"]
points = []

for land_type in landtypes:
    points += generate_graph(df, land_type)

df = pd.DataFrame({
    'county': np.repeat(landtypes, len(dates)),  # repeat land types
    'Geotweets-based Mobility Index (GMI)': points,   # append all the dataframe counts
    'Date': dates * len(landtypes)
})

print(df)
grid(df)

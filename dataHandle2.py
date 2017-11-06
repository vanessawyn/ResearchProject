import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import matplotlib

dfs = []
path = "./Data"
all_files = glob.glob(path + "/*.csv")
frame = pd.DataFrame()

for file_ in all_files:
	df = pd.read_csv(file_, index_col=None, header=0)
	dfs.append(df)
frame = pd.concat(dfs)
frame.to_csv("./merge.csv")
frame = pd.concat(dfs)[[" sa4_name_2016", " SumZScore"]].groupby(' sa4_name_2016').mean()

sa4_bars = frame.sort_values(' SumZScore', ascending=False).plot(kind='bar', figsize=(8,6))
sa4_fig = sa4_bars.get_figure()
plt.xlabel("SA4 Name")
plt.ylabel("Walkability Index")

sa4_fig.tight_layout()


# The figure title
titleName = "SA4 Walkability Index" # --> Editable
sa4_fig.subplots_adjust(top=0.9)
sa4_fig.suptitle(titleName, fontsize=15, fontweight='bold')

plt.show()
sa3_fig.savefig("./figures/sa4_bars.png", dpi=300) # --> Editable
frame.to_csv("./sa4output.csv") # --> Editable

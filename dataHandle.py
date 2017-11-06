import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import matplotlib

#Read and merge CSV files in terms of different study areas
dfs = []
path = "./Data"
all_files = glob.glob(path + "/*.csv")
frame = pd.DataFrame()

for file_ in all_files:
	df = pd.read_csv(file_, index_col=None, header=0)
	dfs.append(df)
frame = pd.concat(dfs)
frame.to_csv("./merge_schoolwalkability.csv")
frame = pd.concat(dfs)[[" sa2_name_2016", " SumZScore"]].groupby(' sa2_name_2016').mean()

# Aggregation visualisation
sa2_bars = frame.sort_values(' SumZScore', ascending=False).plot(kind='bar', figsize=(8,6))
sa2_fig = sa2_bars.get_figure()
plt.xlabel("SA2 Name")
plt.ylabel("Walkability Index")

sa2_fig.tight_layout()

titleName = "SA2 Walkability Index"
sa2_fig.subplots_adjust(top=0.9)
sa2_fig.suptitle(titleName, fontsize=15, fontweight='bold')

plt.show()
sa2_fig.savefig("./figures/sa2_bars.png", dpi=300)

frame.to_csv("./sa2aggregation_output.csv")








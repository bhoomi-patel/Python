import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # more flexible than plain
import pandas as pd 

# data
tips = sns.load_dataset("tips")

#figure and grid
fig = plt.figure(figsize=(20,12), constrained_layout = True)
gs = gridspec.GridSpec(3,4,figure=fig) # 3-row 4-column
fig.suptitle("Seaborn Mini-Dashboard (tips dataset)" , fontsize=20,weight="bold")

# distribution and correlation
ax1 = fig.add_subplot(gs[0,0])
sns.histplot(tips['total_bill'],bins=20,kde=True,ax=ax1)
ax1.set_title("Total-bill hist")

ax2 = fig.add_subplot(gs[0,1])
sns.histplot(tips)

ax2 = fig.add_subplot(gs[0, 1])
sns.histplot(tips["tip"], bins=15, kde=True, color="orange", ax=ax2)
ax2.set_title("Tip hist")

ax3 = fig.add_subplot(gs[0, 2])
sns.kdeplot(data=tips, x="total_bill", hue="time", fill=True, alpha=.6, ax=ax3)
ax3.set_title("KDE by time")

ax4 = fig.add_subplot(gs[0, 3])
corr = tips.select_dtypes("number").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax4)
ax4.set_title("Correlation heatmap")

# categorical summaries
ax5 = fig.add_subplot(gs[1, 0])
sns.boxplot(x="day", y="total_bill", data=tips, ax=ax5)
ax5.set_title("Box • day");  ax5.tick_params(axis="x", rotation=45)

ax6 = fig.add_subplot(gs[1, 1])
sns.violinplot(x="day", y="total_bill", data=tips, ax=ax6)
ax6.set_title("Violin • day"); ax6.tick_params(axis="x", rotation=45)

ax7 = fig.add_subplot(gs[1, 2])
sns.barplot(x="day", y="total_bill", data=tips, ax=ax7)
ax7.set_title("Bar • mean bill"); ax7.tick_params(axis="x", rotation=45)

ax8 = fig.add_subplot(gs[1, 3])
sns.pointplot(x="day", y="total_bill", hue="time", data=tips, ax=ax8)
ax8.set_title("Point • day / time"); ax8.tick_params(axis="x", rotation=45)
ax8.legend(title="time", fontsize=8)

# relationships
ax9  = fig.add_subplot(gs[2, 0])
sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips, ax=ax9)
ax9.set_title("Scatter bill‒tip")

ax10 = fig.add_subplot(gs[2, 1])
sns.regplot(x="total_bill", y="tip", data=tips, ax=ax10)
ax10.set_title("Regression")

ax11 = fig.add_subplot(gs[2, 2])
sns.scatterplot(x="total_bill", y="tip", hue="smoker", style="time",
                data=tips, ax=ax11)
ax11.set_title("Hue + style")
ax11.legend(fontsize=8, title="smoker / time")

ax12 = fig.add_subplot(gs[2, 3])
pivot = tips.pivot_table(values="total_bill",
                         index="day", columns="time", aggfunc="mean")
sns.heatmap(pivot, annot=True, cmap="YlOrRd", fmt=".1f", ax=ax12)
ax12.set_title("Avg bill • day×time")

plt.show()
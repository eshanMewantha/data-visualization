import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data to Dataframe (891 rows)
df = pd.read_csv('../data/titanic/titanic_data.csv')

corr = df.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
plt.show()

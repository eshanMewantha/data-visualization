import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data and split to data fields and target field
df = pd.read_csv('../data/iris/iris_data.csv', index_col=0)

# Draw pair plot
g = sns.pairplot(df, hue="Species", size=2.5)
plt.show()

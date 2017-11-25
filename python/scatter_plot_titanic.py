import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data to Dataframe (891 rows)
df = pd.read_csv('../data/titanic/titanic_data.csv')

# See column names
print(df.columns.values)

# Create a Data frame with only the rows which has a value for 'Age' column (714 rows)
df_age = df.dropna(subset=['Age'])


def draw_scatter_plot(passenger_class):
    g = sns.FacetGrid(df_age[df_age['Pclass'] == passenger_class],
                      col='Sex',
                      col_order=['male', 'female'],
                      hue='Survived',
                      hue_kws=dict(marker=['o', '^']),
                      size=4)
    g = (g.map(plt.scatter, 'Age', 'Fare', edgecolor='w', alpha=0.7, s=80).add_legend())
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('CLASS {}'.format(passenger_class))
    plt.show()

# Visualize the Survival and Non-survival of the first class passengers
draw_scatter_plot(1)

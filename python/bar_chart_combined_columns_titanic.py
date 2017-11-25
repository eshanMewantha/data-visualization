import pandas as pd
import matplotlib.pyplot as plt

# Read data to Dataframe (891 rows)
df = pd.read_csv('../data/titanic/titanic_data.csv')

# See column names
print(df.columns.values)

# Calculate average fare by passenger class and sex
fare_by_class_and_sex = df.groupby(['Pclass', 'Sex'])['Fare'].mean()
print(fare_by_class_and_sex)

# Visualize average fare by class and by gender groups
ax = fare_by_class_and_sex.plot.bar(figsize=(20,6), title='Fare Average by Class and Sex')
ax.set_ylabel('Average Fare')

# rotate x axis labels for better visualization
for tick in ax.get_xticklabels():
    tick.set_rotation(0)

plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data to Dataframe (891 rows)
df = pd.read_csv('../data/titanic/titanic_data.csv')

# See column names
print(df.columns.values)

# Calculate the number of survivors by passenger class
total_survivors_by_class = df.groupby('Pclass')['Survived'].sum()
print(total_survivors_by_class)

# Calculate the number of survivors by passenger sex
total_survivors_by_sex = df.groupby('Sex')['Survived'].sum()
print(total_survivors_by_sex)

# Visualize the Survival and Non-survival of passengers by class and by gender
_, (axis1, axis2) = plt.subplots(1, 2, figsize=(12, 4))

ax = total_survivors_by_class.plot.bar(ax=axis1, color='#5975A4', title='Total Survivors by Class', sharey=True)
ax.set_ylabel('Total Survivors')
ax.set_ylim(0.0, max(total_survivors_by_class) + 10)
ax = total_survivors_by_sex.plot.bar(ax=axis2, color='#5F9E6E', title='Total Survivors by Sex', sharey=True)
ax.set_ylim(0.0, max(total_survivors_by_sex) + 10)

# rotate x axis labels for better visualization
for tick in ax.get_xticklabels():
    tick.set_rotation(0)

plt.show()


from matplotlib import pyplot as plt
import statsmodels.api as sm

df = sm.datasets.get_rdataset('GaltonFamilies', package='HistData').data

# Create a data frame of gender counts
genderCounts = df['gender'].value_counts()

# Plot a bar chart
genderCounts.plot(kind='bar')
plt.xlabel('Gender')
plt.show()

# Create a data frame of child counts
# there's a row for each child, so we need to filter to one row per family to avoid over-counting
families = df[['family', 'children']].drop_duplicates()

# Now count number of rows for each 'children' value, and sort by the index (children)
childCounts = families['children'].value_counts().sort_index()
childCounts.plot(kind='bar', title='Family Size')
plt.xlabel('Number of Children')
plt.ylabel('Families')
plt.show()

# Plot a histogram of father height
df['father'].plot.hist(title='Father Heights')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()

# Create a data frame of heights (father vs child)
heights = df[['midparentHeight', 'childHeight']]
heights.plot(kind='scatter', title='Parent vs Child Heights', x='midparentHeight', y='childHeight')
plt.show()
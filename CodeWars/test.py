import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([184,180,181,184,182,181,182,182,183,182,181,182,182,180,183,181,184,183,182,182,183,182,183,181,180,181,183])
print(df.describe())
print ('Std: ' + str(df.std()))
print ('Min: ' + str(df.min()))
print ('Mode: ' + str(df.mode()[0]))
print ('Median: ' + str(df.median()))
print ('Mean: ' + str(df.mean()))
print ('Max: ' + str(df.max()))

df.plot.hist()
plt.show()
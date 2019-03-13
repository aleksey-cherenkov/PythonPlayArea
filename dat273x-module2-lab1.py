import math
import numpy as np
import numpy.random as nr
from scipy import stats
import matplotlib.pyplot as plt

nr.seed(12345)

nr.normal(10, 2, 50)

sample1 = nr.binomial(1, 0.3, 50)
print(stats.itemfreq(sample1))
np.mean(sample1)

# So the plot appears in line in the noteboook
# %matplotlib inline 

results = [np.mean(nr.binomial(1, 0.3, 50)) for _ in range(100)]
sample_mean = np.mean(results)
plt.hist(results)
plt.vlines(0.3, 0.0, 28.0, color = 'red')
plt.vlines(sample_mean, 0.0, 28.0, color = 'black')
plt.xlabel('Results') 
plt.ylabel('Frequency')
plt.title('Histogram of results')
plt.show()

results_error = [round(x - 0.3, 2) for x in results]
print(results_error)

np.std(results_error)
math.sqrt((.30*(1-.3))/(50-1))
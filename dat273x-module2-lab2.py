import numpy as np
import numpy.random as nr
nr.seed(51120122)

#collect a sample of 100 males
males = nr.normal(5, 3, 100)

#collect a sample of 100 females
females = nr.normal(5, 3, 100)

print(np.mean(males))
print(np.mean(females))
np.mean(males)-np.mean(females)
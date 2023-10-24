import numpy as np

#creating a sample array a
a = np.arange(10) + 5
print(a)

np.random.seed(1)
np.random.shuffle(a)
print(a)

#Returns values from a Standard Normal Distributions
a = np.random.randn(2,3)
print(a)

a = np.random.randint(5,10,3)
print(a)

#Randoly pick one element from a array
element = np.random.choice([1,4,3,2,11,27])
print(element)

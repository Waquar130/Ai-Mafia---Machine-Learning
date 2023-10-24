import numpy as np

#creating a sample array a
a = np.array([[1,2,3,4],[7,6,2,0]])

#finding minimum element in array
print(np.min(a))
print(np.min(a,axis=0))
print(np.min(a,axis=1))

#creating a sample array b
b = np.array([1,2,3,4,5])

#finding mean of array
print(np.mean(b))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))

#creating a sampke array c
c = np.array([1,5,4,2,0])

#finding median of array
print(np.median(c))

# Weighted Mean
# weighted mean => n1*w1 + n2*w2 / n1+n2 
w = np.array([1,1,1,1,1])
print(np.average(c,weights=w))

#finding standard Deviation of array
print(np.std(c))

#finding variance
print(np.var(c))

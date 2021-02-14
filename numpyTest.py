import numpy as np

mylist = [1,2,4,5,6]
arr = np.array(mylist)
arr1 = np.random.randint(1,100,(5,2))
print(arr1)
print(arr1.max())
print(arr1.reshape(2,5))
import numpy as np
np.ones(5)
np.zeros(5)
np.arange(2,100,2)
np.ones(5)*10
np.arange(1,17).reshape(4,4)
np.eye(4)
np.random.rand()*5
np.random.randn(25).reshape(5,5)
np.linspace(1,5,20)
arr = np.arange(1,101).reshape(10,10)
print(arr)
arr[4:]
arr[6:,4:]
arr[:3,2:4]
arr[:3,1]
arr[:3,1:2]
arr[:,9]
arr1 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
arr2 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
print(arr1)
print(arr2)
print(arr1+arr2)
arr1*arr2
arr1.mean()
arr1.sum()

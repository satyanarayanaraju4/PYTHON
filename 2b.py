import numpy as np
arr=np.array([[10,20,5],
             [15,3,25],
             [30,8,12]])
print("original array:")
print(arr)
max_indices=np.argmax(arr,axis=1)
min_indices=np.argmin(arr,axis=1)
print("\nIndices of the maximum values along each row:",max_indices)
print("\nIndices of the minimum values along each row:",min_indices)
max_values=arr[np.arange(len(arr)),max_indices]
min_values=arr[np.arange(len(arr)),min_indices]
print("\nmaximum values:",max_values)
print("minimum values:",min_values)
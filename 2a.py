import numpy as np
data=np.array([12,5,25,7,30,18,9,45,15])
min_val=10
max_val=20
print("originnal array: ",data)
print(f"filtering for numbers between {min_val} and {max_val}...")
filtered_data=data[(data>min_val) & (data<max_val)]
print("extracted numbers:",filtered_data)


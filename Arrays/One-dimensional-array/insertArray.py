import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i', [1,2,3,4,5])
print(my_array1)
my_array1.insert(0,6)
print(my_array1)
my_array1.insert(3,7)
print(my_array1)
my_array1.insert(7,8)
print(my_array1)

import numpy as np
np_array = np.array([], dtype=int)
print(np_array)
np_array1 = np.array([1,2,3,4,5], dtype=int)
print(np_array1)
np_array1 = np.insert(np_array1, 0, 6)
print(np_array1)
np_array1 = np.insert(np_array1, 3, 7)
print(np_array1)
np_array1 = np.insert(np_array1, 7, 8)
print(np_array1)


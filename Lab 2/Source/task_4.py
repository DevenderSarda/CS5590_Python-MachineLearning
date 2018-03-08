from random import randint
import numpy as np
random_array = np.random.randint(0,20, size=(15))
print("Original array: %s"   %random_array)
print("Most Frequent item in the list is", np.bincount(random_array).argmax())
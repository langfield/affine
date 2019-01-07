import sys
import os

import numpy as np

dim = 10


one_hot     = np.array([1 if i == 0 else 0 for i in range(dim)])
next_hot    = np.array([1 if i == 1 else 0 for i in range(dim)])

print("vector")
print(one_hot)
print("transpose")
print(np.transpose(one_hot))

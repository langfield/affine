import affine_funcs
import numpy as np
import math

# PARAMETERS FOR TRANFORMATIONS

def get_config(dim):
    transforms = []
    
    # Argument list for translation transform. 
    # FORMAT: [ direction_vector, magnitude ]
    translation_args = []
    print(np.array([1 if i == 0 else 0 for i in range(dim)]))
    translation_args.append([ np.ones(dim) / math.sqrt(dim), 1 ])
    translation_args.append([ np.zeros(dim) / math.sqrt(dim), 1 ])



    transforms.append([ affine_funcs.translation, np.ones(dim), 1])


if __name__ == '__main__':
    get_config(100)

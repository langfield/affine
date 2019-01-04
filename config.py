import affine_funcs
import numpy as np
import math

# PARAMETERS FOR TRANFORMATIONS

def get_config(dim):
    transforms = []
    
    #=================================

    # TRANSLATION. 
    # FORMAT: [ direction_vector, magnitude ]
    transl_args = [
        [ np.ones(dim) / math.sqrt(dim), 1 ]                           # Vector with all-positive components equidistant from all coordinate axes. 
        [ np.ones(dim) / math.sqrt(dim), 2 ]                            
        [ np.ones(dim) / math.sqrt(dim), 0.5 ]                            
        [ np.ones(dim) / math.sqrt(dim), 0.25 ]                            
        [ np.array([1 if i == 0 else 0 for i in range(dim)]), 1 ]      # 1-hot vector with nonzero value in first dimension. 
        [ np.array([1 if i < 2 else 0 for i in range(dim)]), 1 ]       # 2-hot vector with nonzero values in first 2 dimensions. 
    ]    

    # Append translation config. 
    transforms.append([ affine_funcs.translation, transl_args ])
    
    #=================================

    # HOMOTHETIC TRANSFORM. 
    # FORMAT: [ center, magnitude ]
    # Note: A magnitude of 1 leaves all vectors unchanged. 
    hom_args = [
        [ np.zeros(dim), 2 ]
        [ np.zeros(dim), 0.5 ]
        [ np.ones(dim) / math.sqrt(dim), 1 ]                           # Vector with all-positive components equidistant from all coordinate axes. 
        [ np.ones(dim) / math.sqrt(dim), 2 ]                            
        [ np.ones(dim) / math.sqrt(dim), 0.5 ]                            
        [ np.ones(dim) / math.sqrt(dim), 0.25 ]                            




    ]
      


 
    # Append hom config. 
    transforms.append([ affine_funcs.hom, hom_args ])



if __name__ == '__main__':
    get_config(100)

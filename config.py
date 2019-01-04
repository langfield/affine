import affine_funcs
import numpy as np
import math

# PARAMETERS FOR TRANFORMATIONS

def get_config(dim):
    transforms = []
    
    #=================================

    # TRANSLATION. 
    # FORMAT: [ direction_vector, magnitude ]
    transl_args = []
    transl_args.append([ np.ones(dim) / math.sqrt(dim), 1 ])                           # Vector with all-positive components equidistant from all coordinate axes. 
    transl_args.append([ np.ones(dim) / math.sqrt(dim), 2 ])                            
    transl_args.append([ np.ones(dim) / math.sqrt(dim), 0.5 ])                            
    transl_args.append([ np.ones(dim) / math.sqrt(dim), 0.25 ])                            
    transl_args.append([ np.array([1 if i == 0 else 0 for i in range(dim)]), 1 ])      # 1-hot vector with nonzero value in first dimension. 
    transl_args.append([ np.array([1 if i < 2 else 0 for i in range(dim)]), 1 ])       # 2-hot vector with nonzero values in first 2 dimensions. 
    
    # Append translation config. 
    transforms.append([ affine_funcs.translation, transl_args ])
    
    #=================================

    # HOMOTHETIC TRANSFORM. 
    # FORMAT: [ center, magnitude ]
    hom_args = []
    hom_args.append([ np.ones(dim) / math.sqrt(dim), 1 ])                           # Vector with all-positive components equidistant from all coordinate axes. 
    hom_args.append([ np.ones(dim) / math.sqrt(dim), 2 ])                            
    hom_args.append([ np.ones(dim) / math.sqrt(dim), 0.5 ])                            
    hom_args.append([ np.ones(dim) / math.sqrt(dim), 0.25 ])                            
    hom_args.append([ np.array([1 if i == 0 else 0 for i in range(dim)]), 1 ])      # 1-hot vector with nonzero value in first dimension. 
    hom_args.append([ np.array([1 if i < 2 else 0 for i in range(dim)]), 1 ])       # 2-hot vector with nonzero values in first 2 dimensions. 
    
    # Append hom config. 
    transforms.append([ affine_funcs.hom, hom_args ])



if __name__ == '__main__':
    get_config(100)

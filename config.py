import affine_funcs
import numpy as np
import math

# PARAMETERS FOR TRANFORMATIONS

def get_config(dim):
    transforms = []

    # VECTOR LIBRARY.
    zeroes = np.zeros(dim) 
    diag = np.ones(dim) / math.sqrt(dim)
    one_hot = np.array([1 if i == 0 else 0 for i in range(dim)])
    two_hot = np.array([1 if i < 2 else 0 for i in range(dim)])
    two_hot = two_hot / np.linalg.norn(two_hot) # Normalize. 
    
    #=================================

    # TRANSLATION. 
    # FORMAT: [ direction_vector, magnitude ]
    transl_args = [
        [ diag, 1 ]                           # Vector with all-positive components equidistant from all coordinate axes. 
        [ diag, 2 ]                            
        [ diag, 0.5 ]                            
        [ diag, 0.25 ]                            
        [ one_hot, 1 ]      # 1-hot vector with nonzero value in first dimension. 
        [ two_hot, 1 ]       # 2-hot vector with nonzero values in first 2 dimensions. 
        

    # Append translation config. 
    transforms.append([ affine_funcs.translation, transl_args ])
    
    #=================================

    # HOMOTHETIC TRANSFORM. 
    # FORMAT: [ center, magnitude ]
    # Note: A magnitude of 1 leaves all vectors unchanged. 
    hom_args = [
        [ zeroes, 2 ]
        [ zeroes, 0.5 ]
        [ diag, 2 ]                            
        [ diag, 0.5 ]                            
        [ diag, 0.25 ]                            
    ]
       
    # Append hom config. 
    transforms.append([ affine_funcs.homothetic, hom_args ])

    #=================================

    # REFLECTION. 
    # FORMAT: [ hyperplane_vec ]
    mulan_args = [
        [ np.zeros(dim) ]
        [ diag ]                            
        [ np.array([1 if i == 0 else 0 for i in range(dim)]) ]    
        [ np.array([1 if i < 2 else 0 for i in range(dim)]) ] 
    ]
       
    # Append hom config. 
    transforms.append([ affine_funcs.reflect, mulan_args ])

    #=================================

    # 2-DIMENSIONAL PLANAR ROTATION. 
    # FORMAT: [ u, v, theta ]
    rot_args = [
        [ diag ]                            
        [ np.array([1 if i == 0 else 0 for i in range(dim)]) ]    
        [ np.array([1 if i < 2 else 0 for i in range(dim)]) ] 
    ]
       
    # Append hom config. 
    transforms.append([ affine_funcs.rotate_2D, rot_args ])








if __name__ == '__main__':
    get_config(100)

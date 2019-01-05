import affine_funcs
import numpy as np
import math

# PARAMETERS FOR TRANFORMATIONS

def get_config(dim):
    transforms = []

    pi = np.pi

    # VECTOR LIBRARY.
    zeroes      = np.zeros(dim) 
    diag        = np.ones(dim) / math.sqrt(dim)
    diag_1      = [ -1*val if i == 0 else val for i, val in enumerate(diag) ]
    diag_half   = [ -1*val if i < int(dim/2) else val for i, val in enumerate(diag) ]
    one_hot     = np.array([1 if i == 0 else 0 for i in range(dim)])
    next_hot     = np.array([1 if i == 1 else 0 for i in range(dim)])
    two_hot     = np.array([1 if i < 2 else 0 for i in range(dim)])
    two_hot     = two_hot / np.linalg.norn(two_hot) # Normalize. 
    
    #=================================

    # TRANSLATION. 
    # FORMAT: [ direction_vector, magnitude ]
    transl_args = [
        [ diag, 1 ]     # Vector with all-positive components equidistant from all coordinate axes. 
        [ diag, 2 ]                            
        [ diag, 0.5 ]                            
        [ diag, 0.25 ]                            
        [ one_hot, 1 ]  # 1-hot vector with nonzero value in first dimension. 
        [ two_hot, 1 ]  # 2-hot vector with nonzero values in first 2 dimensions. 
    ]        

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
        [ zeroes ]
        [ diag ]                            
        [ one_hot ]    
        [ two_hot ] 
    ]
       
    # Append hom config. 
    transforms.append([ affine_funcs.reflect, mulan_args ])

    #=================================

    # 2-DIMENSIONAL PLANAR ROTATION. 
    # FORMAT: [ u, v, theta ]
    rot_args = [
        [ diag , diag_1 , pi ]                            
        [ diag , diag_1 , pi/2 ]                            
        [ diag , diag_1 , pi/4 ]                            
        [ diag , diag_1 , pi/6 ]                            
        [ diag , diag_half, pi ]                            
        [ diag , diag_half, pi/2 ]                            
        [ diag , diag_half, pi/4 ]                            
        [ diag , diag_half, pi/6 ]                            
        [ one_hot, next_hot, pi ]    
        [ one_hot, next_hot, pi/2 ]    
    ]
       
    # Append hom config. 
    transforms.append([ affine_funcs.rotate_2D, rot_args ])

if __name__ == '__main__':
    get_config(100)

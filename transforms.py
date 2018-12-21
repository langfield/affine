from preprocessing  import process_embedding
from preprocessing  import check_valid_file
from preprocessing  import check_valid_dir

import numpy as np

from progressbar    import progressbar
from tqdm           import tqdm

import pyemblib
import sympy
import scipy
import time
import sys
import os 

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: a tuple of the script arguments
def parse_args():

    in_path = sys.argv[1]
    out_path = sys.argv[2]
    transform = sys.argv[3]

    args = [in_path,
            out_path,
            transform
            ]

    return args

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: translated matrix. 
def translation(direction, size, matrix):

    # TRANSLATION

    # Generate the translation unit vector. 
    translation_vec = np.zeros(1,100)
    translation_vec[0] = 1   
 
    translation_size = 6
    trans_matrix = []

    # Multiply our unit direction vector by our chosen scale factor. 
    translation_vec = translation_size * translation_vec   
 
    # Apply the translation. 
    for i in range(0, num_rows):     
        trans_matrix[i] = vectors_matrix[i] + translation_vec

    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: Homothetic transform of matrix. 
def homothetic(center, size, matrix):

    # HOMOGENEOUS DILATION

    # For a sample center point, we just use the origin. 
    center = np.zeros(1,100)
    
    dilation_size = 6

    trans_matrix = []

    for i in range(0,num_rows):
        center_diff = vectors_matrix[i] - center
        scaled_center_diff = dilation_size * center_diff
        trans_matrix[i] = center + scaled_center_diff
    
    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: Uniform scale of matrix. 
def uniform_scale(size, matrix):

    # UNIFORM SCALE    
    
    trans_matrix = []

    for i in range(0,num_rows):
        trans_matrix[i] = size * matrix[i]
    
    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# Note that a hyperplane through the origin in R^{n} is defined by a 
# single vector (hyperplane orthogonal to a). 
# RETURNS: Uniform scale of matrix. 
def reflect(hyperplane_vec, matrix):

    # REFLECTION        
    a = hyperplane_vec    
    trans_matrix = []

    for i in range(0,num_rows):
        v = matrix[i]
        reflected_v = v - ((2 * np.dot(v, a) / np.dot(a, a)) * a)
        trans_matrix[i] = reflected_v
    
    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: Rotation of angle theta within the plane specified by
# the two vectors u,v.  
def rotate_2d(u, v, theta, matrix):

    # PLANAR ROTATION IN R^n
    trans_matrix = []

    for i in range(0,num_rows):
        v = matrix[i]
        dimensions = len(v)
        I = np.identity(dimensions) 
        u_transpose = np.flip(u)
        v_transpose = np.flip(v)
        diff_1 = np.multiply(v,u_transpose) - np.multiply(u,v_transpose)
        diff_2 = np.multiply(u,u_transpose) - np.multiply(v,v_transpose)
        summand_1 = np.sin(theta) * diff_1
        summand_2 = (np.cos(theta)  - 1) * diff_2
        trans_matrix = I + summand_1 + summand_2 
    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: Shear mapping of something into something else. 
def shear(u, v, theta, matrix):

    # PLANAR ROTATION IN R^n
    trans_matrix = []

    for i in range(0,num_rows):
        v = matrix[i]
        dimensions = len(v)
        I = np.identity(dimensions) 
        u_transpose = np.flip(u)
        v_transpose = np.flip(v)
        diff_1 = np.multiply(v,u_transpose) - np.multiply(u,v_transpose)
        diff_2 = np.multiply(u,u_transpose) - np.multiply(v,v_transpose)
        summand_1 = np.sin(theta) * diff_1
        summand_2 = (np.cos(theta)  - 1) * diff_2
        trans_matrix = I + summand_1 + summand_2 
    return trans_matrix

#========1=========2=========3=========4=========5=========6=========7==

# RETURNS: transformed matrix. 

def transflow():
     
    check_valid_file(emb_path)
    if os.path.isfile(out_path):
        print("There is already a matrix saved with this name. ")
        exit() 

    # Take the first $n$ most frequent word vectors for a subset. 
    # Set to 0 to take entire embedding. 
    first_n = 0
   
    vectors_matrix,label_df = process_embedding(emb_path,first_n,None)
    num_rows = len(vectors_matrix)

    sample_vector = vectors_matrix[0]
    dimensions = len(sample_vector)

    


    

































from preprocessing  import process_embedding
from preprocessing  import check_valid_file
from preprocessing  import check_valid_dir

import numpy as np

from progressbar    import progressbar
from tqdm           import tqdm

import pyemblib
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

    # Generate the translation unit vector. 
    translation_vec = [1]
    for j in range(1, dimensions):
        translation_vec.append(0)
    
    translation_size = 6

    trans_matrix = []

    for j in range(0, dimensions):
        translation_vec[j] = translation_size * translation_vec[j]
    
    for i in range(0, numrows):
        for j in range(0, dimensions):
            trans_matrix[i][j] = vectors_matrix[i][j] + translation_vec[j]
    


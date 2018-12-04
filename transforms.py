from preprocessing  import process_embedding
from preprocessing  import check_valid_file
from preprocessing  import check_valid_dir

import numpy                        as np

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
    





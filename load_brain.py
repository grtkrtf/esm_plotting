# Script for loading a brain for further manipulation using img_pipe.
# Don't forget to mount dura.
# Also, run this script in interactive mode otherwise it will do nothing.

import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

# A268, EC145, etc.
pid = input('Patient ID: ')
patient = img_pipe.freeCoG(subj=pid, hem='lh')


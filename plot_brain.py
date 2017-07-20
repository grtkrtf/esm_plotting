# Script for simple viewing of a brain.
# Don't forget to mount dura.

import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

# A268, EC145, etc.
pid = input('Patient ID: ')
patient = img_pipe.freeCoG(subj=pid, hem='lh')

# Plotting
patient.plot_brain()

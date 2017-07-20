import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

print("Don't forget to mount dura before running this script ... otherwise it will not work.")

# A268, EC145, etc.
pid = input('Patient ID: ')
patient = img_pipe.freeCoG(subj=pid, hem='lh')

# Plotting
patient.plot_brain()

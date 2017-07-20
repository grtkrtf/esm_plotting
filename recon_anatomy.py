import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

print("Don't forget to mount dura before running this script ... otherwise it will not work.")
print("Also run with -i.")

# prev. EC108
patient = img_pipe.freeCoG(subj='A268',hem='lh')

mesh, mlab = patient.plot_recon_anatomy(elecfile_prefix='A268_syntax_stim_surface_warped',
                           template='cvs_avg35_inMNI152',
                           showfig=False,
                           screenshot=True)
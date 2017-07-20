# Script for generating a figure with electrodes on it.
# Don't forget to mount dura.

import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

# Edit these values to change which subject/electrodes to grab.
# I am lazy so you'll have to define the ROIs manually.
subj = 'cvs_avg35_inMNI152'
hem = 'lh'
elecfile_prefix = 'garret_syntax'
template = 'cvs_avg35_inMNI152'

# Get electrodes
patient = img_pipe.freeCoG(subj = subj, hem = hem)
elecs = patient.get_elecs(elecfile_prefix=(elecfile_prefix))['elecmatrix']

# Load the recon
atlas_patient = img_pipe.freeCoG(subj=template, hem = hem)

# Define ROIs and color them
pial = atlas_patient.roi('pial',opacity=1, representation='surface',color=(0.8,0.8,0.8),gaussian=False)
tri = atlas_patient.roi('lh_parstriangularis',opacity=0.5, representation='surface',color=(1.0,0.5,0.5),gaussian=False)
op = atlas_patient.roi('lh_parsopercularis',opacity=0.5, representation='surface',color=(0.5,0.5,1.0),gaussian=False)

# Plotting
atlas_patient.plot_brain(rois = [pial,tri,op],
                         showfig = True,
                         screenshot = True,
                         elecs = elecs)

# Script for generating a figure with electrodes and ROIs on it.
# Similar to figure.py but modular -- allows plotting of elecs from any subject.
# Don't forget to mount dura.

import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

subjs = ['A208','A223','EC106','A232','A235','A268','A281','EC145']
# EC106 = A231
# EC145 = A268_2

elecs = []

# get the electrode coordinate matrix for each subject
for s in subjs:
    print s
    patient = img_pipe.freeCoG(subj = s, hem = 'lh')
    elecs.append(patient.get_elecs(elecfile_prefix=('%s_syntax_stim_surface_warped'%(s)))['elecmatrix'])

# combine the electrode matrices from the different subjects into one matrix
elecmatrix = np.concatenate(elecs, axis=0)


# Load template brain
template = 'cvs_avg35_inMNI152'
atlas_patient = img_pipe.freeCoG(subj=template, hem ='lh')


# Define ROIs.
pial = atlas_patient.roi('pial',opacity=1, representation='surface',color=(0.8,0.8,0.8),gaussian=False)
tri = atlas_patient.roi('lh_parstriangularis',opacity=0.5, representation='surface',color=(1.0,0.5,0.5),gaussian=False)
op = atlas_patient.roi('lh_parsopercularis',opacity=0.5, representation='surface',color=(0.5,0.5,1.0),gaussian=False)

# Plotting
atlas_patient.plot_brain(rois = [pial,tri,op],
                         showfig = True,
                         screenshot = True,
                         elecs = elecmatrix)

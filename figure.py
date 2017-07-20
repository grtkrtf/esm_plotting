import os
import img_pipe
from mayavi import mlab
import scipy.io
import numpy as np

print("Don't forget to mount dura before running this script ... otherwise it will not work.")

# sneaky way to get elecs
patient = img_pipe.freeCoG(subj = 'cvs_avg35_inMNI152', hem = 'lh')
elecs = patient.get_elecs(elecfile_prefix=('garret_syntax'))['elecmatrix']

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
                         elecs = elecs)

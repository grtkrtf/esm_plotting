# run with pythonw

import os
from mayavi import mlab
import numpy as np
import scipy.io
import img_pipe

# syntax subjs: https://docs.google.com/spreadsheets/d/1JlK0eCOr38tjnRd-4WuDI0OaQ78V866hZASzjuwEvoo/edit?usp=sharing
subjs = ['A208','A223','EC106','A232','A235','A268','A281','EC145','A293']
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

# pass elecmatrix to plot_brain()
template = 'cvs_avg35_inMNI152'
atlas_patient = img_pipe.freeCoG(subj=template, hem ='lh')
roi = atlas_patient.roi('pial',opacity=1)
atlas_patient.plot_brain(rois = [roi],
                         showfig = True,
                         screenshot = True,
                         elecs = elecmatrix)
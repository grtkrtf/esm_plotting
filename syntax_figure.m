% script for plotting syntax figure.
% Nonstandard ctmr_gauss plot is used here in order to deal with weird
% lighting. Credit goes to Jon Kleen!

cd ~/Documents/MATLAB/plotting

% load and plot right hemisphere
load cvs_avg35_inMNI152_rh_pial
ctmr_gauss_plot_jk(cortex,[0 0 0], 0, 'rh');
hold on

% load and plot left hemisphere
load cvs_avg35_inMNI152_lh_pial
ctmr_gauss_plot_jk(cortex,[0 0 0], 0, 'lh');

% Set figure background to white
set(gcf,'Color','w');

% load electrodes and moves them slightly off the surface of the cortex so
% they are more visible
load plot2brain.mat
elecmatrix(:,1) = elecmatrix(:,1)-2

% Plots electrodes with black outline for visibility
el_add(elecmatrix(), 'color', 'black', 'msize',11, 'numbers',[]);
el_add(elecmatrix(), 'color', 'red', 'msize',6, 'numbers',[]);
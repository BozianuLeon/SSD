import numpy as np 
import pandas as pd
import os

import matplotlib.pyplot as plt
import matplotlib

from plot_boxes import make_box_metric_plots
from plot_phys import make_phys_plots
from plot_jets import make_jet_plots


folder_to_look_in = "/home/users/b/bozianu/work/SSD/SSD/cached_inference/SSD_model_10_large_mu/20230912-14"
save_at = "/home/users/b/bozianu/work/SSD/SSD/cached_metrics/SSD_model_10_large_mu/"


if __name__=="__main__":
    print('Making plots about boxes')
    make_box_metric_plots(folder_to_look_in,save_at)
    print('Completed plots about boxes\n')
    print('Making physics plots')
    make_phys_plots(folder_to_look_in,save_at)
    print('Completed physics plots\n')
    print('Making jet plots')
    make_jet_plots(folder_to_look_in,save_at)
    print('Completed jet plots\n')


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

import pymc as pm


bookmark = np.loadtxt("./data/bookmark.csv", dtype = int, delimiter = ",")

bookmark_collumns = [
        "id", "user_id", "origin_id", "translation_id", "text_id", 
        "fit_for_study", "learning_cycle", "level","user_preference"
            ]



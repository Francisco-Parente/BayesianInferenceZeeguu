import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

import pymc as pm


bookmark = np.genfromtxt("./data/bookmark.csv", dtype = int, delimiter = ",")
bookmarkTranslations = np.genfromtxt("./data/bookmarkTranslations.csv", dtype = int, delimiter = ",")

bookmarkCollumns = [
        "id", "user_id", "origin_id", "translation_id", "text_id", 
        "fit_for_study", "learning_cycle", "level","user_preference"
            ]
bookmarkTranslationsCollumns = ["user_id", "origin_id", "count(origin_id)"]

x = bookmarkTranslations[:,0]
y = bookmarkTranslations[:,2]

with pm.Model() as model:

    sigma = pm.HalfCauchy("sigma", beta=10)
    intercept = pm.Normal("Intercept", 0, sigma=20)
    slope = pm.Normal("slope", 0, sigma=20)

    likelihood = pm.Normal("y", mu=intercept + slope * x, sigma=sigma, observed=y)

    idata = pm.sample(3000)



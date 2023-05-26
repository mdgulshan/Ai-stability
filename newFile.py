import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from darts import TimeSeries 
import sklearn.metrics as metrics
from sklearn.metrics import mean_absolute_percentage_error

from darts.models import Prophet
from darts.models import NBEATSModel
from darts.models import NHiTSModel

data= pd.read_excel('Train.xlsx')
data

filtered_df = data.loc[(data['date'] >= '2018-10-01')
                     & (data['date'] < '2021-10-31')]

print(len(filtered_df))
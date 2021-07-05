import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import pyplot as plt
from sklearn import model_selection
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

import math
import pandas as pd
import numpy as np
from IPython.display import display
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import TimeSeriesSplit

data = pd.read_csv('dataset.csv')
dataset_train=data.iloc[0:1125,2:]
dataset_test=data.iloc[1125:,2:]
training_set = data.iloc[0:1125, 2:].values
testing_set=data.iloc[1125:,2:].values
data.head()

data.drop('SystemCodeNumber', axis=1, inplace=True)
data.drop('Capacity', axis=1, inplace=True)
print(data.head())
data.to_csv('tata_preprocessed.csv',index= False)
data = data.iloc[::-1]

plt.figure(figsize = (25,15))
plt.plot(range(data.shape[0]),(data['Occupancy']))
plt.xticks(range(0,data.shape[0],500),data['LastUpdated'].loc[::500],rotation=45)
plt.xlabel('LastUpdated',fontsize=18)
plt.ylabel('Occupancy',fontsize=18)
plt.show()

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)
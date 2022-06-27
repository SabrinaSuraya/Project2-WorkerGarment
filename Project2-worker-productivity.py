# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:59:52 2022

@author: sabri
"""

import sklearn.datasets as skdatasets
from sklearn import preprocessing
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers, optimizers, losses, metrics
#import tensorflow_transform as tft
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
import datetime, os
import pandas as pd

#read data from csv
file_path= r"C:\Users\sabri\Documents\PYTHON\DL\Datasets\garments_worker_productivity.csv"
worker_data= pd.read_csv(file_path, sep=',', header= 0 )

#%%
#View teh first 5 data
worker_data.head()
#%%
#Check null in all column
print(worker_data.isna().sum())

#null is present in the wip column
#%%
#perform Data Cleaning
#(a) Drop less useful columns
worker_data= worker_data.drop(['date', 'quarter', 'day'], axis= 1)

#worker_data= worker_data.wip.fillna(worker_data.wip.mean())
#(d) Replace missing values in Title column
worker_data = worker_data.fillna(value={'wip':worker_data['wip'].mean()})

print(worker_data.isna().sum())
#DATA CLEANING IS DONE
#%%
worker_data['actual_productivity'].value_counts()
#is not classification is regression problme

#%%
#DATA PREPROCESSING
#%%

#Use One Hot Label
worker_data = pd.get_dummies(worker_data)
#%%
#5. Split into features and labels
feature= worker_data.copy()
label= worker_data.pop('actual_productivity')



#%%

#train & test split

SEED=12345
x_train, x_test, y_train, y_test= train_test_split(feature, label, test_size=0.2, random_state=SEED)


#DAta normalisation
standardizer = StandardScaler()
standardizer.fit(x_train)
x_train= standardizer.transform(x_train)
x_test= standardizer.transform(x_test)

##DATA PREPARATION IS COMPLETED

#%%
#4. Construct NN model

#Use sequential API
model= keras.Sequential()
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1))


#%%

#9. Compile and train the model
base_log_path = r"C:\Users\sabri\Documents\PYTHON\DL\TensorBoard\tb_logs"
log_path = os.path.join(base_log_path, datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+ '___Project2')
tb = TensorBoard(log_dir=log_path)
es= EarlyStopping(monitor='val_loss',patience=10) 

model.compile(optimizer='adam',loss='mse')
history = model.fit(x_train,y_train,validation_data=(x_test,y_test),batch_size=16,epochs=200,callbacks=[tb, es])












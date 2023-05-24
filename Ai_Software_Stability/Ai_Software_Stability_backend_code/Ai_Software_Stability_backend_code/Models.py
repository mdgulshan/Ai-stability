import os
os.environ['CURL_CA_BUNDLE'] = ''

import pandas as pd
import numpy as np
import datetime
import nltk
from nltk import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from darts.models import Prophet
from darts.models import NBEATSModel
from darts.models import ExponentialSmoothing
from darts import TimeSeries
from pandas import to_datetime
from datetime import datetime
#from fbprophet.diagnostics import cross_validation
import pickle
import string
import re



# def build_model_n_beats(df41, dataset_name):
#      print("dataset_name",dataset_name)
#      print("df41", df41)
#      df41 = df41.drop(columns=['Site Name'])
#      print("df41", df41)
#      df41 = df41.rename(columns={'date': 'ds', 'Weekly_Count': 'y'})
#      print("df41", df41)
#      df41['ds'] = pd.to_datetime(df41.ds)
#      train_size = int(len(df41) * 0.8)
#      train_df = df41[:train_size]
#      test_df = df41[train_size:]
#      train_series = TimeSeries.from_dataframe(train_df, 'ds', 'y')
#      test_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
#      model_nbeattry = NBEATSModel(input_chunk_length=720, output_chunk_length=24)
#      model_nbeattry.fit(train_series)
#      file_path = os.path.join('model_folder', f'{dataset_name}_n_beats.pkl')
#      with open(file_path, 'wb') as f:
#         pickle.dump(model_nbeattry, f)
#      train_complete2 = f"Model Training using N-beats Completed for {dataset_name}"
#      return train_complete2
    
current_dateTime = datetime.now()
date_t = str(current_dateTime.year)+'_'+ str(current_dateTime.month)+'_'+ str(current_dateTime.day)+'_' +str(current_dateTime.hour)+'_' + str(current_dateTime.minute)+'_'+str(current_dateTime.second)
       
print(date_t) # 2022

  
def build_model_facebook_prophet(df41,dataset_name):
    print("dataset_name",dataset_name)
    print("df41", df41)
    df41 = df41.drop(columns=['Site Name'])
    print("df41", df41)
    df41 = df41.rename(columns={'date': 'ds', 'Weekly_Count': 'y'})
    #df41.columns = ['ds', 'y']
    print("df41", df41)
    df41['ds'] = pd.to_datetime(df41.ds)

    #use when you have no data for testing 
#     train_size = int(len(df41) * 0.8)
#     train_df = df41[:train_size]
#     test_df = df41[train_size:]
    
    train_df= df41.copy()
    train_series = TimeSeries.from_dataframe(train_df, 'ds', 'y')
    #test_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
    model = Prophet()
    model.fit(train_series)
    #cv_results = cross_validation(model, initial='730 days', period='180 days', horizon='365 days')
    file_path = os.path.join('Training_model_folder', f'{dataset_name}_facebook_prophet.pkl')
    with open(file_path, 'wb') as files:
        pickle.dump(model, files, protocol=4)
    # with open('model_pkl', 'wb') as files:
    #     pickle.dump(model, files)
       
    train_complete1=f"Model Training using Facebook Prophet Completed for {dataset_name}"
    return train_complete1


def build_model_exponential(df41,dataset_name):
    print("dataset_name",dataset_name)
    print("df41", df41)
    df41 = df41.drop(columns=['Site Name'])
    print("df41", df41)
    df41 = df41.rename(columns={'date': 'ds', 'Weekly_Count': 'y'})
    #df41.columns = ['ds', 'y']
    print("df41", df41)
    df41['ds'] = pd.to_datetime(df41.ds)

    #use when you have no data for testing 
#     train_size = int(len(df41) * 0.8)
#     train_df = df41[:train_size]
#     test_df = df41[train_size:]
    
    train_df= df41.copy()
    train_series = TimeSeries.from_dataframe(train_df, 'ds', 'y')
    #test_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
    expo = ExponentialSmoothing()
    expo.fit(train_series)
    #cv_results = cross_validation(model, initial='730 days', period='180 days', horizon='365 days')
    
    file_path = os.path.join('Training_model_folder', f'{dataset_name}_exponential.pkl')
    print("file_path:", file_path)
    try:
         if not os.path.exists('Training_model_folder'):
            os.makedirs('Training_model_folder')
         with open(file_path, 'wb') as file:
             pickle.dump(expo, file,protocol=4)
       
         print("File saved successfully.")
    # Check if the Training_model_folder directory exists
   

    # Save the file
    

    except Exception as e:
         print("Error saving the file:", e)
   
    # with open(file_path, 'wb') as files:
    #     pickle.dump(expo, files)
    # with open('expo_pkl', 'wb') as files:
    #     pickle.dump(expo, files)
    train_complete1=f"Model Training using exponential smoothning Completed for {dataset_name}"
    return train_complete1

# def build_model_facebook_prophet_test(df41,dataset_name):
#     print("dataset_name",dataset_name)
#     print("df41", df41)
#     df41 = df41.drop(columns=['Site Name'])
#     print("df41", df41)
#     df41 = df41.rename(columns={'date': 'ds', 'Weekly_Count': 'y'})
#     #df41.columns = ['ds', 'y']
#     print("df41", df41)
#     df41['ds'] = pd.to_datetime(df41.ds)

#     #use when you have no data for testing 
# #     train_size = int(len(df41) * 0.8)
# #     train_df = df41[:train_size]
# #     test_df = df41[train_size:]
    
#     train_df= df41.copy()
#     train_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
#     #test_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
#     model = Prophet()
#     model.fit(train_series)
#     #cv_results = cross_validation(model, initial='730 days', period='180 days', horizon='365 days')
#     file_path = os.path.join('Testing_model_folder', f'{dataset_name}_facebook_prophet_{date_t}.pkl')
#     with open(file_path, 'wb') as files:
#         pickle.dump(model, files)
#     # with open('model_pkl', 'wb') as files:
#     #     pickle.dump(model, files)
       
#     test_complete1=f"Model Testing using Facebook Prophet Completed for {dataset_name}"
#     return test_complete1

# def build_model_exponential_test(df41,dataset_name):
#     print("dataset_name",dataset_name)
#     print("df41", df41)
#     df41 = df41.drop(columns=['Site Name'])
#     print("df41", df41)
#     df41 = df41.rename(columns={'date': 'ds', 'Weekly_Count': 'y'})
#     #df41.columns = ['ds', 'y']
#     print("df41", df41)
#     df41['ds'] = pd.to_datetime(df41.ds)

#     #use when you have no data for testing 
# #     train_size = int(len(df41) * 0.8)
# #     train_df = df41[:train_size]
# #     test_df = df41[train_size:]
    
#     train_df= df41.copy()
#     train_series = TimeSeries.from_dataframe(train_df, 'ds', 'y')
#     #test_series = TimeSeries.from_dataframe(test_df, 'ds', 'y')
#     expo = ExponentialSmoothing()
#     expo.fit(train_series)
#     #cv_results = cross_validation(model, initial='730 days', period='180 days', horizon='365 days')
    
#     file_path = os.path.join('Testing_model_folder', f'{dataset_name}_exponential.pkl')
#     print("file_path:", file_path)
#     try:
#          if not os.path.exists('Testing_model_folder'):
#             os.makedirs('Testing_model_folder')
#          with open(file_path, 'wb') as file:
#              pickle.dump(expo, file)
       
#          print("File saved successfully.")
#     # Check if the Training_model_folder directory exists
   

#     # Save the file
    

#     except Exception as e:
#          print("Error saving the file:", e)
   
#     # with open(file_path, 'wb') as files:
#     #     pickle.dump(expo, files)
#     # with open('expo_pkl', 'wb') as files:
#     #     pickle.dump(expo, files)
#     test_complete1=f"Model Testing using exponential smoothning Completed for {dataset_name}"
#     return test_complete1
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
from darts import TimeSeries 

def Split_DataIn_Interval_WeekWise_test(df,site_name):
  df1=pd.DataFrame(columns=['Number','Site Name','Short description','date'])
  l1=[]
  l2=[]
  l3=[]
  l4=[]
  for i in range(len(df)):
    if(df['Site Name'].iloc[i]==site_name):
      #a1=[df['Number'].iloc[i], df['Site Name'].iloc[i], df['Short description'].iloc[i], df['date'].iloc[i]]


      l1.append(df['Number'].iloc[i])
      l2.append(df['Site Name'].iloc[i])
      l3.append(df['Short description'][i])
      l4.append(df['Created'].iloc[i])

      #df1.append(pd.Series(a1), ignore_index=True)
      #df1.append(a1)


  df1['Number']=l1
  df1['Site Name']=l2
  df1['Short description']=l3
  df1['date']=l4

  dataset = df1[["date"]]
  dataset['Created'] = pd.to_datetime(df1['date']).dt.date
  dataset.sort_values("date")
  dataset['date'] = pd.to_datetime(dataset['Created']).dt.date
  dataset['date'] = pd.to_datetime(dataset.date)
  dataset['Weekly_Count']=1
  dataset['year'] = dataset['date'].dt.year
  dataset['month'] = dataset['date'].dt.month
  dataset['day_of_month'] = dataset['date'].dt.day
  dataset['day_of_week'] = dataset['date'].dt.dayofweek
  dataset['Week Number of year'] =dataset['date'].dt.isocalendar().week
  # print("dataset",dataset)

  group_data = dataset.groupby(['year','Week Number of year'])['Week Number of year'].count() #sum function

  return dataset

def week_wise_split_test(df1,site_name):
  # data_week = Split_DataIn_Interval_WeekWise_train(data,'MLO-500 : MLO - Cheshire')
  data_week = Split_DataIn_Interval_WeekWise_test(df1,site_name)
  print(data_week)
  print(data_week.columns)
  data_week = data_week.groupby(pd.Grouper(key='date', freq='W')).count()
  #data_week=data_week.resample('W', on='date').count()
  data_week=data_week.drop(['Created','year','month','day_of_month','day_of_week','Week Number of year'],axis=1)
  data_week.reset_index(inplace=True)
  data_week['Site Name'] = site_name

  return data_week
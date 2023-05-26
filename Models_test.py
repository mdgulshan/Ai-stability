import numpy as np
import pandas as pd
import pickle



from datetime import datetime, timedelta


# def original_test_data(start_date, end_date, dataset_name):
#     data_path = f'Testing_model_folder/{dataset_name}.csv' 
#     data = pd.read_csv(data_path)

#     # data = pd.read_csv(r'C:\Users\US67204\PycharmProjects\pythonProject\macy\dataset\site_Name_Portland.csv')
#     #data_path = f'dataset_file/{dataset_name}.csv'
#     #data_path = f'C:\\Users\\vg59563\\Desktop\\macy-backend\\dataset_file\\{dataset_name}.csv'
#     #data = pd.read_csv(data_path)
#     data['date'] = pd.to_datetime(data['date'])
#     print("Data", data)
#     #start_date_2021 = pd.to_datetime(start_date).replace(year=2021)
#     #end_date_2021 = pd.to_datetime(end_date).replace(year=2021)
#     # print("end_date_2020",end_date_2020)

#     data_prev_year = data[(data['date'] >= pd.to_datetime(start_date)) & (data['date'] <= pd.to_datetime(end_date))]
#     data_prev_year = data_prev_year[['date', 'Weekly_Count']]
#     print("data_2020", data_prev_year)

#     return data_prev_year


def prophet_prediction(model_Prophet,interval):
    prediction_Prophet = model_Prophet.predict(interval)
    return prediction_Prophet

    
def exponential_prediction(model_exponential,interval):
    prediction_Exponential = model_exponential.predict(interval)
    return prediction_Exponential
    

def get_7day_intervals(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    intervals = []
    current_date = start_date
    while current_date < end_date:
        #interval = (current_date, current_date + timedelta(days=7))
        intervals.append(current_date)
        current_date = (current_date + timedelta(days=7))
        #intervals.append(current_date)
        #intervals.append(interval)
        #current_date += timedelta(days=7)
    #intervals.append((current_date, end_date)) # Adding the last interval
    #intervals.append(current_date)
    return intervals



# r is test data if it exists skip line 63 to 72
def predict_7day_dataset(start_date, end_date, dataset_name, *r1):
#     print("start_date", start_date)
#     print("end_date", end_date)
#     print("dataset_name", dataset_name)
#     print(type(dataset_name))
    start_date1 = datetime.strptime(start_date, "%a, %d %b %Y %H:%M:%S GMT")
    end_date1 = datetime.strptime(end_date, "%a, %d %b %Y %H:%M:%S GMT")
    start_date1 = start_date1.strftime("%Y-%m-%d")
    end_date1 = end_date1.strftime("%Y-%m-%d")
    date_difference = datetime.strptime(end_date1, "%Y-%m-%d") - datetime.strptime(start_date1, "%Y-%m-%d")
    #print(date_difference)

    intervals = get_7day_intervals(start_date1, end_date1)

    interval_count = len(intervals)
    
#     data_path = f'dataset_file/{dataset_name}.csv'
#     #data_path = f'C:\\Users\\vg59563\\Desktop\\macy-backend\\dataset_file\\{dataset_name}.csv'
#     data = pd.read_csv(data_path)
#     print(f"dataset loaded name is",{dataset_name})
#     print(f"{dataset_name}", data)

#     # Get number of intervals between max_date and 5 days before start_date
#     max_date = data.date.max()
#     start_minus_max = datetime.strptime(start_date1, "%Y-%m-%d") - timedelta(days=1)
#     max_to_start_minus_max = get_7day_intervals(max_date, start_minus_max.strftime("%Y-%m-%d"))
#     max_to_start_minus_max_count = len(max_to_start_minus_max)

#     # Add the two interval counts to get the total range for the loop
#     total_interval_count = interval_count + max_to_start_minus_max_count

#     past_values = 10

    
    
    model_path_prophet = f"Training_model_folder/{dataset_name}_facebook_prophet.pkl"
    #print(type(model_path_prophet))
    #print(model_path_prophet)
    
    model_path_exponential = f"Training_model_folder/{dataset_name}_exponential.pkl" 
    #print(type(model_path_exponential))
    #print(model_path_exponential)
    
    # model_file_prophet = pickle.load(open(model_path_prophet,'rb'))
    # model_file_exponential = pickle.load(open(model_path_exponential,'rb'))
    with open(model_path_prophet , 'rb') as file:
        model_file_prophet = pickle.load(file,encoding="latin1")
    with open(model_path_exponential, 'rb') as file:
        model_file_exponential = pickle.load(file,encoding="latin1")    
    #print(model_file_prophet) 
    #print(model_file_exponential) 
    #print(interval_count)
    #print(intervals)
    #print('###################')      
    output_prophet = prophet_prediction(model_file_prophet,interval_count)
    output_exponential = exponential_prediction(model_file_exponential,interval_count)
    #print(output_prophet)
    #print(output_exponential)
#     data_weekly=pd.DataFrame(columns=['Actual', 'Prophet', 'NBEATS','NHiTSModel','Predicted'],index=range(len(test_series2)))
    data_weekly=pd.DataFrame(columns=['Predicted_Date','Prophet', 'Exponential','Predicted_Count'],index=range(interval_count))
    #data_prev_year = original_test_data(start_date,end_date,dataset_name)
    for i in range(interval_count):
        data_weekly['Predicted_Date'][i]= intervals[i]
        data_weekly['Predicted_Date'][i] =  data_weekly['Predicted_Date'][i].date()
        data_weekly['Predicted_Date'][i] =  data_weekly['Predicted_Date'][i].strftime('%d-%m-%Y')
        data_weekly['Prophet'][i] = output_prophet.univariate_values(copy=True, sample=0)[i]
        data_weekly['Exponential'][i] = output_exponential.univariate_values(copy=True, sample=0)[i]
        data_weekly['Predicted_Count'][i] = round((data_weekly['Prophet'][i] + data_weekly['Exponential'][i])/2)
    
    data_weekly2= data_weekly[['Predicted_Date','Predicted_Count']]
    # data_weekly2['Actual_Date'] = data_prev_year['date']
    # data_weekly2['Actual_Count'] = data_prev_year['Weekly_Count']
    # print("Data_weekly2", data_weekly2)
    return data_weekly2.to_dict('records')
        
        
    print(data_weekly)
    
    
    
    
    

    
start = "Sat, 01 Jan 2022 18:30:00 GMT"

end = "Mon, 28 Jan 2022 18:30:00 GMT"     
    
#predict_7day_dataset(start, end, 'Chesire')    
    
def predict_7day_dataset_test(start_date, end_date, dataset_name):
#     print("start_date", start_date)
#     print("end_date", end_date)
#     print("dataset_name", dataset_name)
#     print(type(dataset_name))
    # start_date1 = datetime.strptime(start_date, "%a, %d %b %Y %H:%M:%S GMT")
    # end_date1 = datetime.strptime(end_date, "%a, %d %b %Y %H:%M:%S GMT")
    # start_date1 = start_date1.strftime("%Y-%m-%d")
    # end_date1 = end_date1.strftime("%Y-%m-%d")
    # date_difference = datetime.strptime(end_date1, "%Y-%m-%d") - datetime.strptime(start_date1, "%Y-%m-%d")
    # #print(date_difference)

    # intervals = get_7day_intervals(start_date1, end_date1)

    # interval_count = len(intervals)
    
    
    model_path_prophet = f"Training_model_folder/{dataset_name}_facebook_prophet.pkl"
    #print(type(model_path_prophet))
    #print(model_path_prophet)
    
    model_path_exponential = f"Training_model_folder/{dataset_name}_exponential.pkl" 
    #print(type(model_path_exponential))
    #print(model_path_exponential)
    
    # model_file_prophet = pickle.load(open(model_path_prophet,'rb'))
    # model_file_exponential = pickle.load(open(model_path_exponential,'rb'))
    with open(model_path_prophet , 'rb') as file:
        model_file_prophet = pickle.load(file)
    with open(model_path_exponential, 'rb') as file:
        model_file_exponential = pickle.load(file)    
    #print(model_file_prophet) 
    #print(model_file_exponential) 
    #print(interval_count)
    #print(intervals)
    #print('###################')      
    output_prophet = prophet_prediction(model_file_prophet,interval_count)
    output_exponential = exponential_prediction(model_file_exponential,interval_count)
    #print(output_prophet)
    #print(output_exponential)
#     data_weekly=pd.DataFrame(columns=['Actual', 'Prophet', 'NBEATS','NHiTSModel','Predicted'],index=range(len(test_series2)))
    data_weekly=pd.DataFrame(columns=['Predicted_Date','Prophet', 'Exponential','Predicted_Count'],index=range(interval_count))
    data_prev_year = original_test_data(dataset_name,start_date1,end_date1)
    for i in range(interval_count):
        data_weekly['Predicted_Date'][i]= intervals[i]
        data_weekly['Prophet'][i] = output_prophet.univariate_values(copy=True, sample=0)[i]
        data_weekly['Exponential'][i] = output_exponential.univariate_values(copy=True, sample=0)[i]
        data_weekly['Predicted_Count'][i] = round((data_weekly['Prophet'][i] + data_weekly['Exponential'][i])/2)
    
    data_weekly2= data_weekly[['Predicted_Date','Predicted_Count']]
    data_weekly2['Actual_Date'] = data_prev_year['date']
    data_weekly2['Actual_Count'] = data_prev_year['Weekly_Count']
    print(data_weekly) 
    print("Data_weekly2", data_weekly2)
    return data_weekly2.to_dict('records')
        
        
    print(data_weekly) 
    
    
#     model_path = f"Training_model_folder/{dataset_name}_Bidirectional_LSTM_Multivariate.h5"
#     print(f"h5 filename is loaded name is", {model_path})
#     model = load_model(model_path)
#     X_scaler = MinMaxScaler()
#     Y_scaler = MinMaxScaler()

#     data['date'] = pd.to_datetime(data['date'])
#     data['year'] = data['date'].dt.year
#     data['month'] = data['date'].dt.month
#     # data['day_of_week'] = data['date'].dt.dayofweek
#     data['day_of_month'] = data['date'].dt.day
#     # hist_window =6
#     print("df41", data)
#     print("df41. datatypes",data.dtypes)
#     data=data.drop(columns=['date','Site Name'])

#     pred_list = []
#     for i in range(total_interval_count):
#         X_scaler.fit(data.tail(past_values + i))
#         data_val = X_scaler.transform(data.tail(past_values))
#         val_rescaled = data_val.reshape(1, data_val.shape[0], data_val.shape[1])
#         pred = model.predict(val_rescaled, verbose=0)
#         Y_scaler.fit(data[['count']])
#         pred_Inverse = Y_scaler.inverse_transform(pred)
#         pred_list.append(int(pred_Inverse[0][0]))

#     predicted_df = pd.DataFrame({
#         "predicted_Date": [interval[0].strftime("%Y-%m-%d") for interval in intervals],
#         "Predicted_count": pred_list[-interval_count:]
#     })
#     print("predicted_df",predicted_df)
#     try:
#         data_prev_year = original_data(dataset_name,start_date1,end_date1)


#         df_forecast = pd.DataFrame({
#             "predictions_date": [interval[0].strftime("%Y-%m-%d") for interval in intervals],
#             "predicted_count": pred_list[-interval_count],
#             'past_dates': data_prev_year['date'],
#             'past_count': data_prev_year['count']
#         })

#         df_forecast['past_dates'] = pd.to_datetime(df_forecast['past_dates'])
#         df_forecast['past_dates'] = df_forecast['past_dates'].dt.strftime('%Y-%m-%d')


#         print(df_forecast)
#         return df_forecast.to_dict('records')
#     except:

#         return predicted_df.to_dict('records')

# # start = "Sat, 01 Jan 2022 18:30:00 GMT"
# # end = "Mon, 06 Jan 2022 18:30:00 GMT"
# #
# # print(predict_5day_dataset(start, end,'site_Name_Cheshire'))

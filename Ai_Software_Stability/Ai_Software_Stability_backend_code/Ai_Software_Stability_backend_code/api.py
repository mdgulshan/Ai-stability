# from  fastapi.responses import JSONResponse
# from fastapi import FastAPI, UploadFile, File, Form, requests
# import pandas as pd
# # from starlette import requests
# from BertApi import *
# from test import print_5day_intervals
# from train import build_model
# from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# origins = [

#     "http://localhost:3000",
#     "http://localhost:3001",
#     "http://localhost:8080",
#     "http://localhost:8000"

# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],

# )
# list1=[]
# past_values=0


# @app.post("/Read_csv/")
# async def read_input(csv_file: UploadFile = File(...),look_back: int = Form(...),future_prediction: int = Form(...)):

# # Read the CSV file into a Pandas dataframe
#     df = pd.read_csv(csv_file.file,encoding="latin1")
#     # global past_values
#     # past_values=look_back
#     # list1.append(past_values)
#     result=build_model(df,look_back,future_prediction)


#     return str(result)


# # print("past_values3", past_values)

# @app.post("/predict/")
# async def predict(start_date: str = Form(),end_date: str = Form()):
#     global past_values

#     print("past_values of predict ",past_values)
#     # print("past_values4", past_values)
#     start=start_date
#     end=end_date
#     result=print_5day_intervals(start, end)
#     return result


# def ngram(df):
#     try:
#         from bertopic import BERTopic
#         topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
#         topics, probs = topic_model.fit_transform(list_short_all)
#     except:
#         # df_two=pd.read_excel('bigramcsvcount_1.xlsx')
#         # df_one=pd.read_excel('onegramcount.xlsx')
#         df_three = pd.read_excel(r'C:\Users\vg59563\Desktop\macy-backend\trigramcount.xlsx')
#         df_three = df_three[['Trigram', 'Count']]

#     return df_three.head(20).to_dict('records')



# @app.post("/trigramdf")
# # csv_file: UploadFile = File(...),look_back: int = Form(...),future_prediction: int = Form(...)
# async def read_input2(csv_file: UploadFile = File(...)):  # Read the CSV file into a Pandas dataframe
#     dfg = pd.read_csv(csv_file.file, encoding='latin1')
#     dfg = dfg[['Number', 'Priority', 'Incident state', 'Short description', 'Resolution notes']]

#     # print(dfg.columns)

#     # return dfg.head(20).to_dict('records')
#     return ngram(dfg)
from  fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File, Form, requests
import pandas as pd
import io
# from starlette import requests
from fastapi.responses import HTMLResponse
from BertApi import *
from resampling_7d import Split_DataIn_Interval_WeekWise_train
from resampling_7d import week_wise_split_train
from Resample_test import Split_DataIn_Interval_WeekWise_test
from Resample_test import week_wise_split_test
#from test import predict_5day_intervals
#from test_site_Name import predict_5day_dataset
from Models_test import predict_7day_dataset
from Models_test import *
#from train import build_model
# from site_Name import build_model_site_Name
# from site_Name import build_model_facebook_prophet
# from site_Name import build_model_n_beats
from Models import build_model_exponential
from Models import build_model_facebook_prophet
# from Models import build_model_exponential_test
# from Models import build_model_facebook_prophet_test

import os


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [

    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8080",
    "http://localhost:8000"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
list1=[]
past_values=0





def ngram(df):
    try:
        from bertopic import BERTopic
        topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
        topics, probs = topic_model.fit_transform(list_short_all)
    except:
        # df_two=pd.read_excel('bigramcsvcount_1.xlsx')
        # df_one=pd.read_excel('onegramcount.xlsx')
        df_three = pd.read_excel(r'C:\Users\US67204\PycharmProjects\pythonProject\macy\dataset\trigramcount.xlsx')
        df_three = df_three[['Trigram', 'Count']]

    return df_three.head(20).to_dict('records')



@app.post("/trigramdf")
# csv_file: UploadFile = File(...),look_back: int = Form(...),future_prediction: int = Form(...)
async def read_input2(csv_file: UploadFile = File(...)):  # Read the CSV file into a Pandas dataframe
    dfg = pd.read_csv(csv_file.file, encoding='latin1')

    dfg = dfg[['Number', 'Priority', 'Incident state', 'Short description', 'Resolution notes']]

    # print(dfg.columns)
    # return dfg.head(20).to_dict('records')
    return ngram(dfg)



# for next 5models
@app.post("/Read_csv_site_Name/")
async def site_Name(excel_file: UploadFile = File(...),dataset: str = Form(...)):

# Read the CSV file into a Pandas dataframe
    #dataset_name = csv_file.filename
    print("hello")
    print("upload_file",excel_file)
    print("hii")
    print("Dataset_Name", dataset)
    print("Bye")

    df = pd.read_excel(excel_file.file.read())
   

    df11 = week_wise_split_train(df, dataset)

    print("df11",df11)
    if(dataset=='MLO-869 : MLO - Tulsa'):
        dataset='Tulsa'
    elif(dataset=='MLO-050 MLO - Portland'):
        dataset="Portland"
    elif(dataset=='MLO-043 : MLO - West Virginia'):
        dataset="West_Virginia"
    elif(dataset=='MLO-506 : MLO - Goodyear'):
        dataset="Goodyear"
    elif(dataset=='MLO-500 : MLO - Cheshire'):
        dataset="Chesire"
    else:
        dataset="None"
   
    result1 = build_model_facebook_prophet(df11,dataset)
    result2 = build_model_exponential(df11,dataset)
    #return str(result1)
    return JSONResponse(content={"result1": result1, "result2": result2})

@app.post("/Read_csv_site_Name_test/")
async def site_Name(excel_file: UploadFile = File(...),dataset: str = Form(...)):

# Read the CSV file into a Pandas dataframe
    #dataset_name = csv_file.filename

    df = pd.read_excel(excel_file.file.read())
   
    # file_content = await excel_file.read()
    # df311 = pd.read_excel(io.BytesIO(file_content), engine='openpyxl')
    
    #needs full dataset below -- eg 'MLO-500 : MLO - Cheshire'
    test_df = week_wise_split_test(df, dataset)

    # cwd = os.getcwd()
    # csv_name = '/CONTCAR_SORTED'
    # df12 = pd.read_csv(f"{cwd}{csv_name}",
    #                 skiprows=2, nrows=100, names=['X','Y','Z' ], 
    #                 delimiter='\s+',engine='python')

    # /df11.to_csv(os.path.join(cwd, "new"))
    
    #test_df.to_csv(r'C:\Users\vg59563\Downloads\macy-backend (4) (1)\macy-backend (5)\macy-backend (3)\macy-backend (2)\macy-backend\{dataset}.csv')
    directory = os.path.join(os.getcwd(), "Testing_model_folder")
    if not os.path.exists(directory):
         os.makedirs(directory)
    if(dataset=='MLO-869 : MLO - Tulsa'):
        dataset='Tulsa'
    elif(dataset=='MLO-050 : MLO - Portland'):
        dataset="Portland"
    elif(dataset=='MLO-043 : MLO - West Virginia'):
        dataset="West_Virginia"
    elif(dataset=='MLO-506 : MLO - Goodyear'):
        dataset="Goodyear"
    elif(dataset=='MLO-500 : MLO - Cheshire'):
        dataset="Chesire"
    else:
        dataset="None"
    file_path = os.path.join(directory, f"{dataset}.csv")
    test_df.to_csv(file_path)


    print("Test data 7d interval ",test_df)



    # if(dataset=='MLO-869 : MLO - Tulsa'):
    #     dataset='Tulsa'
    # elif(dataset=='MLO-050 MLO - Portland'):
    #     dataset="Portland"
    # elif(dataset=='MLO-043 : MLO - West Virginia'):
    #     dataset="West_Virginia"
    # elif(dataset=='MLO-506 : MLO - Goodyear'):
    #     dataset="Goodyear"
    # elif(dataset=='MLO-500 : MLO - Cheshire'):
    #     dataset="Chesire"
    # else:
    #     dataset="None"

   
    # result2 = build_model_facebook_prophet_test(df11,dataset)
    # result3 = build_model_exponential_test(df11,dataset)
    #return str(test_df)
    return "hello"
    #return JSONResponse(content={"result2": result2, "result3": result3})




@app.post("/predict_site_Name/")
async def predict_site_Name(start_date: str = Form(), end_date: str = Form(), dataset: str = Form(...)):
    global past_values
    print("start_date", start_date)
    print("End_date", end_date)
    print("dataset", dataset)
    print("past_values of predict ",past_values)
    start = start_date
    end = end_date
    if(dataset=='MLO-869  MLO - Tulsa'):
        dataset='Tulsa'
    elif(dataset=='MLO-050  MLO - Portland'):
        dataset="Portland"
    elif(dataset=='MLO-043  MLO - West Virginia'):
        dataset="West_Virginia"
    elif(dataset=='MLO-506  MLO - Goodyear'):
        dataset="Goodyear"
    elif(dataset=='MLO-500  MLO - Cheshire'):
        dataset="Chesire"
    else:
        dataset="None"
    print('dataset', dataset)
    # r1= original_test_data(start, end, dataset)
    # print("r1",r1)
    #result = predict_7day_dataset(start, end, dataset, r1)
    result = predict_7day_dataset(start, end, dataset)
    return result
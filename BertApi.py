#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install bertopic


# In[2]:


import pandas as pd



# In[3]:





# In[4]:









# In[5]:


#df=pd.read_csv('Incidentdump_OnlyIncidents_AllMegas_2018_2021.csv',encoding='latin1')


# In[6]:


# list_short_all=[]
# for i in range(len(df)):
#      list_short_all.append(df['Short description'].iloc[i])  


# In[7]:

def ngram(df):
    try:
        from bertopic import BERTopic
        topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
        topics, probs = topic_model.fit_transform(list_short_all)
    except:
        # df_two=pd.read_excel('bigramcsvcount_1.xlsx')
        # df_one=pd.read_excel('onegramcount.xlsx')
        df_three=pd.read_excel('trigramcount.xlsx')
        df_three=df_three[['Trigram','Count']]
    
    
    return df_three.head(20).to_dict('records')


# try:
#     topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
#     topics, probs = topic_model.fit_transform(list_short_all)
# except:
#     df_two=pd.read_excel('bigramcsvcount_1.xlsx')
#     df_one=pd.read_excel('onegramcount.xlsx')
#     df_three=pd.read_excel('trigramcount.xlsx')
#     df_three=df_three[['Trigram','Count']]
#     print("In except block")
#     print(df_three)



# In[ ]:

from fastapi import FastAPI, UploadFile, File, Form, requests
from BertApi import *
    
app=FastAPI()

@app.get("/")
async def read_input1():

    return str("Welcome")

# @app.get("/Trigram")
# async def read_input():
    
#     # return str(df_three)
#     return df_three.head(20).to_dict('records')

# @app.get("/Bigram")
# async def read_input():
    
#     # return str(df_three)
#     return df_two.head(20).to_dict('records')

# @app.get("/Onegram")
# async def read_input():
    
#     # return str(df_three)
#     return df_one.head(20).to_dict('records')

@app.post("/trigramdf")
#csv_file: UploadFile = File(...),look_back: int = Form(...),future_prediction: int = Form(...)
async def read_input2(csv_file: UploadFile = File(...)):# Read the CSV file into a Pandas dataframe
    dfg=pd.read_csv(csv_file.file, encoding='latin1')
    dfg=dfg[['Number', 'Priority', 'Incident state', 'Short description', 'Resolution notes']]
    
    #print(dfg.columns)

    #return dfg.head(20).to_dict('records')
    return ngram(dfg)

# import csv
# import codecs

# @app.post("/upload")
# def upload(file: UploadFile = File(...)):
#     csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
#     data = {}
#     for rows in csvReader:             
#         key = rows['Id']  # Assuming a column named 'Id' to be the primary key
#         data[key] = rows  
    
#     file.file.close()
#     return data

# In[ ]:





# In[ ]:


# topic_model.visualize_topics()


# In[ ]:


# dict1=topic_model.get_representative_docs()  #open when topic model works


# In[ ]:


# df1= pd.DataFrame.from_dict(dict1,orient = 'index',columns=['data1','data2','data3'])


# In[ ]:


# df4 = pd.DataFrame({'topic': topics, 'document': list_short_all})


# In[ ]:


# df4=df4.sort_index()
# df4=df4.sort_values(by='topic')


# In[ ]:


# df1['Data']=''
# x = lambda a, b, c : a + ' ' + b + ' ' + c + ' '
# x2 = lambda a : a + ' '
# for i in range(len(df1)):
#     df1['Data'].iloc[i] = x(df1['data1'].iloc[i],df1['data2'].iloc[i],df1['data2'].iloc[i])
#     df1['Data'].iloc[i]=df1['Data'].iloc[i].lower()
# df1 = df1.sort_index()
# df1


# In[ ]:


# l1=len(topic_model.get_topic_info())

# for i in range(l1 - 1):
#     item = df4[df4.topic == i]
#     for j in range(3):
#       a= (item['document'].iloc[j])
#       df1['Data'].iloc[i]=   df1['Data'].iloc[i] + x2(a)
#       df1['Data'].iloc[i]=df1['Data'].iloc[i].lower()


# In[ ]:





# In[ ]:


# !pip install yake


# In[ ]:


# import yake
# kw_extractor = yake.KeywordExtractor()


# In[ ]:


# df_bigram_yake = pd.DataFrame(columns=['Ngram'],index=range(len(df1)))


# In[ ]:


# for i in range(len(df1)):
#     df_bigram_yake['Ngram'][i]= kw_extractor.extract_keywords(df1['Data'].iloc[i])
# #     print(i," : ",df_bigram_yake['Ngram'][i])
# #     print()


# In[ ]:


# output = df_bigram_yake.to_dict()


# In[ ]:


# listall=[]
# for i in range(len(output['Ngram'])):
#     value = output['Ngram'][i]
#     for j in range(len(value)):
#         listall.append(output['Ngram'][i][j][0])
        

# listall = set(listall)
# listall = list(listall)


# In[ ]:


# l1=[]
# l2=[]
# l3=[]
# for i in range(len(listall)):
#     h=listall[i].count(" ")
#     if(h==0):
#         l1.append(listall[i])
#     elif(h==1):
#         l2.append(listall[i])
#     elif(h==2):
#         l3.append(listall[i])
#     else:
#         print("More sapces")


# In[ ]:


# print(" Len all: ",len(listall))
# print(" Len onegram: ", len(l1))
# print(" Len bigram: ", len(l2))
# print(" Len trigram: ", len(l3))


# In[ ]:


# df_onegram = pd.DataFrame(l1,columns=['Onegram'],index=range(len(l1)))
# df_bigram = pd.DataFrame(l2,columns=['Bigram'],index=range(len(l2)))
# df_trigram = pd.DataFrame(l3,columns=['Trigram'],index=range(len(l3)))
# df_bigram['Count']=0
# df_trigram['Count']=0
# df_onegram['Count']=0


# In[ ]:


# def Counter(a):
#     ct=0
#     for i in range(len(df)):
#         value = df11['Description'][i]
#         value=value.lower()
#         ct += value.count(a)
#     return ct   


# In[ ]:


# for i in range(len(df_onegram)):
#     item = df_onegram['Onegram'].iloc[i]
#     df_onegram['Count'][i] = Counter(item)
    
# df_onegram=df_onegram.sort_values(by='Count',ascending=False)  


# In[ ]:


# for i in range(len(df_bigram)):
#     item = df_bigram['Bigram'].iloc[i]
#     df_bigram['Count'][i] =  Counter(item)
    
# df_bigram=df_bigram.sort_values(by='Count',ascending=False)    


# In[ ]:


# for i in range(len(df_trigram)):
#     item = df_trigram['Trigram'].iloc[i]
#     df_trigram['Count'][i] =  Counter(item)
       
    
# df_trigram=df_trigram.sort_values(by='Count',ascending=False)    


# In[ ]:


# df_onegram.head(50)


# In[ ]:


# df_bigram.head(50)


# In[ ]:


# df_trigram.head(50)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# SSLError: HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /sentence-transformers/all-MiniLM-L6-v2/resolve/7dbbc90392e2f80f3d3c277d6e90027e55de9125/1_Pooling/config.json (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1125)')))


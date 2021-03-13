#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from  keras.models import load_model


# In[2]:


def Mlist(data):
    x =len(data)-1
    a = [data.iloc[i][3] for i in range(x-100,x)]+[data.iloc[x][3]]
    b = [data.iloc[i][5] for i in range(x-100,x)]+[data.iloc[x][3]]
    c = [data.iloc[i][2] for i in range(x-100,x)]+[data.iloc[x][3]]
    d = [data.iloc[i][4] for i in range(x-100,x)]+[data.iloc[x][3]]
    mylist=[a,b,c,d]
    return mylist


# In[3]:


def predict(csv):
    
    data = pd.read_csv(str(csv))
    x = np.array(Mlist(data))
    predict_data  = np.expand_dims(x,axis=0)
    try:
        model
    except NameError:
        model = load_model('model.h5')        
    result = model.predict(predict_data)
    trend = np.argmax(result)
    probability = result[0][trend]*100
    return str(trend), str(probability)


# In[ ]:





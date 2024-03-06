import pickle
import json
import numpy as np
__location=None
__data_column=None
_model=None

def get_estemted_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_column.index(location.lower())
    except ValueError:
        loc_index = -1
       
    x=np.zeros(len(__data_column))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(_model.predict([x])[0],2)
    
#we use this for requesting and responsing  a data 
def get_location():
    return __location
def load_artifacts():
    global __location,__data_column,_model
    
    with open("C:/Users/Ivar/Desktop/django/PRACTICE/server/artifacts/coloumns.json",'r') as f:
       __data_column= json.load(f)['data_columns']
       __location=__data_column[3:]
    with open ('C:/Users/Ivar/Desktop/django/PRACTICE/server/artifacts/Bengaluru_House_Data.pickle','rb') as f:
         _model=pickle.load(f)
    print(' the files are loaded')

if __name__=="__main__":
    load_artifacts()
 
    print(get_location())
    print(get_estemted_price('1st block koramangala',1000,2,2))
    print(get_estemted_price('alur',1000,3,2))
    print(' python sever')
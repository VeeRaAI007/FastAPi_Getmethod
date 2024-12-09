from typing import Optional
from fastapi import FastAPI

app_fast = FastAPI()

@app_fast.get("/")
def home():
  return {"name":"Prasad","city":'HYD' }

@app_fast.get('/items/')
def list_items():
  return {'cars':'Honda','engine_typte':'v9'}
  
@app_fast.get('/items/{item_id}')
def tems(item_id:int):
  return {'id':item_id,'cars':['suv','swift','benz'],'engine_typte':'v9'}


@app_fast.get('/clients/')
def client_details(limit:int=10,active:bool=True,emergency:Optional[str]=None,skip:int=2):
  return {'clients':'{} client_details available.'.format(limit),'active':active,'emergency':emergency,'skipped':skip}



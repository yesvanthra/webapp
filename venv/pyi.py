from fastapi import FastAPI
from pydantic import BaseModel,Field
#from typing import Optional
from datetime import date

app = FastAPI()
user_db={
    'yesva':{'username':'yesvanthra','location':'chennai','age':'25'},
    'adhvik':{'username':'adhvik rian','location':'andaman','age':'3'}
}
#pydanticmodel
class User(BaseModel):
    username:str#=Field(min_length=3,max_length=20)
    #date_joined:date
    location:str#Optional[str]=None
    age:int#=Field(None,gt=5,lt=130)

@app.get("/")
def read_root():
    return {"hello":"welcome"}
#@app.get('/users')
#def get_users():
    #user_list=list(user_db.values())
    #return user_list

#to filter a particular username
@app.get('/users/{username}')
def get_users_path(username:str):
    return user_db[username]
# query users based on criteria:query parameter
@app.get('/users')
def get_users_query(limit:int=20):#we can set int=2
    user_load=list(user_db.values())
    return user_load[:limit]


#using post operation
@app.post('/users')
def create_user(user:User):
    usernames=user.username
    user_db[usernames]=user.dict()
    return {'message':f'successfully created user:{usernames}'}

#delete parameter to delete data
@app.delete('/users/{username}')
def delete_user(username:str):
    del user_db[username]
    return {'message':f'successfully deleted user:{username}'}

# put operation
@app.put('/users')
def update_user(user:User):
    username=user.username
    user_db[username]=user.dict()
    return{'message':f'succesfully update:{username}'}
print("hello world")
print("hi ")

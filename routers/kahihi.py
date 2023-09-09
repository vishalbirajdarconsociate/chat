from pydantic import BaseModel
from fastapi import FastAPI, Request


app = FastAPI()
user="demo"
pas="demo"
token_getter =1312
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/login/{username}/{password}")
def read_post(username, password):
    print(username , password)
    if username != user or password != pas:
        return "not fount"
    # token_getter=+10
    return  token_getter


@app.get("/chat/{token}/{chat}")
def token_get(token, chat):
    print()
    if int(token) == token_getter:
        #chat logic 
        return token
    else:
        return "token"
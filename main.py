import datetime
from fastapi import FastAPI
from routers import airouter
from starlette.responses import Response
from starlette.status import HTTP_200_OK
from pydantic import BaseModel
from src import manageUser

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/skyhubdocs", redoc_url=None)
app.include_router(airouter.router)

@app.get("/")
def getRoot(response: Response):

    response.status_code = HTTP_200_OK
    return

class UserInfo(BaseModel):
    email: str
    password: str
    name: str = None
    birth: str = None
    gender: str = None
    nickname: str = None

@app.post("/register")
def register(userInfo: UserInfo, response: Response):
    if userInfo.birth:
        userInfo.birth = datetime.datetime.strptime(userInfo.birth, "%Y-%m-%d")

    response.status_code, result = manageUser.ManageUser().registerUser(userInfo)

    return result

class UserLoginInfo(BaseModel):
    identifier: str
    password: str

@app.post("/login/")
def login(userLoginInfo: UserLoginInfo, response: Response):

    response.status_code, result = manageUser.ManageUser().loginUser(userLoginInfo)

    return result

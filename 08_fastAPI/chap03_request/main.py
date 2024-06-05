
# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문 (body)사용

# 단순 텍스트나 json 을 사용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class UserInfo(BaseModel):
    name : str
    password : str
    url : Optional[HttpUrl] = None #옵셔널은 선택사항 기본URL은 None이다.
# UserInfo 클래스 (BaseInfo 을 상속 받음)
# BaseModel 을 상속 받아야 request body 부분에 받을 클래스로 이용할 수 있음



# 이 요청은 post받는 바디 부분을 userinfo로 받을거다 클래스 자료형으로 user라는 객체로 받을거다.
@app.post("/users")
def createUser(user:UserInfo):
    return user


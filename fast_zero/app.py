from http import HTTPStatus
from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}    

@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import token
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(data:str=Depends(oauth2_schema)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,details="could not validate credentials",header={"www-Authenticals":"Bearer"})
    return token.verify_token(data,credentials_exception)

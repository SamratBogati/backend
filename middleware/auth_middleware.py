from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    print(payload)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload["sub"]
 
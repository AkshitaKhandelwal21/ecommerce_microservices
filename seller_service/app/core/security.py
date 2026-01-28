from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
import jwt

from app.core.config import settings


security = HTTPBearer()

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials

    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_id: int = payload.get('user_id') or payload.get('sub')
        if user_id is None:
            raise HTTPException(status_code=404)
        return user_id

    except JWTError:
        raise HTTPException(status_code=401)
import requests
from functools import wraps
import streamlit as st
from .auth_config import AuthConfig 


def grant_access(func):
    @wraps(func)
    def wrapper(token: str, details: dict, *args, **kwargs): 
        """
        Verifies user credentials and allows access to the specified resource upon 
        successful validation of the user's token. The Authentication Service returns 
        specific responses based on the token's validity:

         - When the token is valid, the response will be: {"permission_granted": "TOKEN_ACCEPTED"}
         - If the token is invalid, the response will be: {"permission_denied": "TOKEN_DENIED"}
        """

        headers = {
            "user_token": token,
            "service_name": AuthConfig.SERVICE_NAME,
            "permission_name": "access"
        }

        r = requests.post(
            url=AuthConfig.AUTH_SERVICE_URL,
            headers=headers,
            json=details
        )

        # if token correct resposne contains: {"permission_granted": "TOKEN_ACCEPTED"}
        # if token is wrong response contains: {"permission_denied": "TOKEN_DENIED"}
        if AuthConfig.VALIDATION_ON:
            response = r.json()
            access = response.get("permission_granted", False) if r.status_code == 200 else False

        # for testing purposes
        else :
            access = True

        if access:
            return func(*args, **kwargs)
        
        return st.error("You do not have access to this resource")

    return wrapper

    

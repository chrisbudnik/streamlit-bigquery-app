import requests
from functools import wraps
import streamlit as st
from .auth_config import AuthConfig 
from .permission_roles import AuthPermissionRole


def grant_access(func):
    @wraps(func)
    def wrapper(
        token: str, 
        details: dict, 
        role: AuthPermissionRole,
        *args, **kwargs
    ) -> bool: 

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
            "permission_name": role.value
        }

        r = requests.post(
            url=AuthConfig.AUTH_SERVICE_URL,
            headers=headers,
            json=details
        )

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

    

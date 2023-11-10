from enum import Enum


class AuthPermissionRole(Enum):
    USER = 'user'
    SENDER = 'sender'  
    ADMIN = 'admin'
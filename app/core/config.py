import os
from datetime import timedelta
from jose import JWTError, jwt

SECRET_KEY = "super_secret_key_poné_algo_muy_largo_acá"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

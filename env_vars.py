import os

sk = os.environ.get('SECRET_KEY')
dv = os.environ.get('DEBUG_VALUE')
print(sk,dv)
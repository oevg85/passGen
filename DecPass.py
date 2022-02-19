import sys
from cryptography.fernet import Fernet
import hashlib
import base64

secret = 'barsik'

def decrypt(pasW):
    f = Fernet(base64.urlsafe_b64encode(hashlib.md5(secret.encode()).hexdigest().encode("utf-8")))
    token = f.decrypt(pasW)    
    print(token.decode())

if __name__ == "__main__":
    decrypt((sys.argv[1]).encode())
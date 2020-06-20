from cryptography.fernet import Fernet
from fff_automation.modules import settings

settings.set_encryption()

def encrypt(value):
    """
    Accepts any string or integer
    Returns a cyphered string
    """
    key = settings.get_var('CRYPTO_KEY').encode('UTF-8')
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(str(value).encode('UTF-8'))
    plain_text = bytes(ciphered_text).decode('utf-8')
    print(plain_text)
    return plain_text


def decrypt(value):
    """
    Accepts as input a bytes variable.
    Returns a string
    """
    key = settings.get_var('CRYPTO_KEY').encode('UTF-8')
    cipher_suite = Fernet(key)
    uncipher_text = cipher_suite.decrypt(value.encode('UTF-8'))
    plain_text = bytes(uncipher_text).decode('utf-8')
    print(plain_text)
    try:
        result = int(plain_text)
    except:
        result = str(plain_text)
    return result
import secrets

def generate_access_key():
    print(secrets.token_urlsafe(32))

generate_access_key()

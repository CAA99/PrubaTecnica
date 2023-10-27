from jwt import encode, decode

def create_token(data : dict):
    token: str = encode(payload=data, key="4EFC42133CD4E3CF293B8BB4ECD6F", algorithm="HS256")
    return token

def validate_token(token:str) -> dict:
    data: dict = decode(token, key="4EFC42133CD4E3CF293B8BB4ECD6F", algorithms=['HS256'])
    return data
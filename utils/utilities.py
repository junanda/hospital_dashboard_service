import uuid

def generate_id(usr:str) -> str:
    namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
    uid_obj = str(uuid.uuid3(namespace, usr))
    return uid_obj.replace('-', '')
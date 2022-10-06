import re


async def check_email(email):
    if(len(email) < 3):
        return False

    regex = r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$'

    if(re.match(regex, email)):
        return True
    
    return False
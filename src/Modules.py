import json


def dba(self, message):
    with open('alist.json', 'w') as f:

        user = json.load(f)

    return user[str(message.author.id)]
    
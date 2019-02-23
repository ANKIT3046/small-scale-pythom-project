import json

data='''
{
    "name":"ankit",
    "phone":{
        "type":"intl",
        "number":"+91 8701774667"
    },
    "email":{
        "hide":"yes"
    }
}
'''
info=json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

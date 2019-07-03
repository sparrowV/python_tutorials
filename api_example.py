import requests

def getSummary(users,params):
    result = {}
    for user in users:
        paramValueList = []
        for paramName in params:
            paramValueList.append(user[paramName])
        result[user['id']] =paramValueList
    return result

response = requests.get("https://jsonplaceholder.typicode.com/users",timeout = 3)
response_data = response.json()
print(len(response_data))
if(response.ok):
    summary = getSummary(response_data,['name','email','phone','website'])
    print(summary)
else:
    print("some error happend",response.status_code)
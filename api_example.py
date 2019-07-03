import requests

def getSummary(users,params):
    result = {}
    for user in users:
        result[user['id']] =user['name']+" , "+user['phone']
    return result

response = requests.get("https://jsonplaceholder.typicode.com/users",timeout = 3)
response_data = response.json()
print(len(response_data))
summary = getSummary(response_data)
print(summary)
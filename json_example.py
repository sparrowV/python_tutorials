import json
import requests_example
# f = open("example.json")
json_string = '''
    {
  "countries":[
    {
      "name":"usa",
      "capital":"washingot",
      "west": true
    },
    {
      "name":"canada",
      "capital":"ottawa",
      "west": true
    },
    {
      "name":"japan",
      "capital":"Tokyo",
      "west": false
    }
  ]

}
'''

json_data =  json.loads(json_string)
# print(type(json_data))
# countries = json_data['countries']
# print(countries)
# for country in countries:
#     print(country['name'],country['capital'])

# json_string_from_dict = json.dumps(json_data,indent = 4,sort_keys=True)
# print(json_string_from_dict)
f = open("dump.json","w")
json.dump(json_data,f,indent= 4,sort_keys=True)

json.loads()
json.load()

json.dumps()
json.dump()
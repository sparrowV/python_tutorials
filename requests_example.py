import requests

response_data = requests.get("https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg")
# print(response_data.text)
# print(response_data.content)
# print(response_data.headers['content-type'])
print(response_data.content)
f = open("my_image.jpeg","wb")
f.write(response_data.content)
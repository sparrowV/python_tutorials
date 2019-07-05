import requests


post = {"userId":1,"title":" my title","body":"this is post body"}

response = requests.post("https://jsonplaceholder.typicode.com/posts",data=post)
print(response.text)
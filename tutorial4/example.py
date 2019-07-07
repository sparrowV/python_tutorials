import requests
import sqlite3

def getUserIdWithMostPosts(posts):
    postNumbersForUsers = {}
    for post in posts:
        userId = post['userId']
        if(userId in postNumbersForUsers):
            postNumbersForUsers[userId]+=1
        else:
            postNumbersForUsers[userId] = 1


    maxPostsUserId = None
    maxPosts = 0
    for key in postNumbersForUsers:
        if(postNumbersForUsers[key] > maxPosts):
            maxPosts = postNumbersForUsers[key]
            maxPostsUserId = key

    return maxPostsUserId


response = requests.get("https://jsonplaceholder.typicode.com/posts",timeout = 6)
if(response.ok):
    posts = response.json()
    print(getUserIdWithMostPosts(posts))
    print(posts)
else:
    print("error with status code: ",response.status_code)
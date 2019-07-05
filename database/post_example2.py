import sqlite3 as db

class Post:
    def __init__(self,title,body,author):
        self.title = title
        self.body = body
        self.author = author


connection = db.connect('posts.db')
cursor = connection.cursor()





posts_table = '''
    CREATE TABLE Posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title text,
        body text,
        author text
    );
'''
cursor.execute(posts_table)
title = input("enter post title: ")
body = input("enter post body: ")
author = input("enter post title: ")
post = Post(title,body,author)

insert_post = " insert into posts(title,body,author) values(:title,:body,:author)"
cursor.execute(insert_post,{'title':post.title,'body':post.body,'author':post.author})
connection.commit()
cursor.close()
connection.close()

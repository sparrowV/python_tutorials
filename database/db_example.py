import sqlite3 as db

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
connection.commit()
cursor.close()
connection.close()

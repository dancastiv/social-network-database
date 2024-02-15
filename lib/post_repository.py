from lib.post import Post

class PostRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute('SELECT * FROM posts;')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['account_id'])
            posts.append(item)
        return posts
    
    def find(self, id):
        rows = self._db_connection.execute('SELECT * FROM posts WHERE id = %s;', [id])
        row = rows[0]
        return Post(row['id'], row['title'], row['content'], row['views'], row['account_id'])
    
    def create(self, post):
        self._db_connection.execute('INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s);', [post.title, post.content, post.views, post.account_id])

    def delete(self, id):
        self._db_connection.execute('DELETE FROM posts WHERE id = %s', [id])

    def all_posts(self, account_id):
        rows = self._db_connection.execute('SELECT * FROM posts WHERE account_id = %s;', [account_id])
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['account_id'])
            posts.append(item)
        return posts
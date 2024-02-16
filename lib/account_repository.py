from lib.account import Account
from lib.post import Post

class AccountRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute('SELECT * FROM accounts;')
        accounts = []
        for row in rows:
            item = Account(row['id'], row['email_address'], row['username'])
            accounts.append(item)
        return accounts
    
    def find(self, id):
        rows = self._db_connection.execute('SELECT * FROM accounts WHERE id = %s;', [id])
        row = rows[0]
        return Account(row['id'], row['email_address'], row['username'])
    
    def create(self, account):
        self._db_connection.execute('INSERT INTO accounts (email_address, username) VALUES (%s, %s);', [account.email_address, account.username])

    def delete(self, id):
        self._db_connection.execute('DELETE FROM accounts WHERE id = %s', [id])

    def find_with_posts(self, id):
        rows = self._db_connection.execute('SELECT accounts.id AS account_id, email_address, username, posts.id AS post_id, title, content, views FROM accounts JOIN posts ON accounts.id = posts.account_id WHERE accounts.id = %s;', [id])
        posts = []
        for row in rows:
            post = Post(row['post_id'], row['title'], row['content'], row['views'], row['account_id'])
            posts.append(post)
        return Account(rows[0]['account_id'], rows[0]['email_address'], rows[0]['username'], posts)
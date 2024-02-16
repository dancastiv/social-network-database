from lib.database_connection import DatabaseConnection
from lib.account_repository import AccountRepository
from lib.post import Post


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/social_network.sql")

    def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
        
        print('Welcome to the Luna Nova Social Network\n')
        print('Select a user to show their posts:')

        account_repository = AccountRepository(self._connection)
        accounts = account_repository.all()
        for account in accounts:
            print(f'* {account.id} - {account.username}')
        
        choice = input('Enter your choice by ID:')
        account_with_posts = account_repository.find_with_posts(choice)
        print(account_with_posts.username+ '\n')
        for post in account_with_posts.posts:
            print(post.title)
            print(post.content)
            print(f'Views: {post.views}\n')

if __name__ == '__main__':
        app = Application()
        app.run()
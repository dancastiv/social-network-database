class Account:
    def __init__(self, id, email_address, username, posts = []):
        self.id = id
        self.email_address = email_address
        self.username = username
        self.posts = posts

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Account({self.id}, {self.email_address}, {self.username}, {self.posts})'

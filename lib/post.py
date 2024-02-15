class Post():
    def __init__(self, id, title, content, views, account_id):
        self.id = id
        self.title = title
        self.content = content
        self.views = views
        self.account_id = account_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Account({self.id}, {self.title}, {self.content}, {self.views}, {self.account_id})'

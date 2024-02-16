from lib.account_repository import AccountRepository
from lib.account import Account
from lib.post import Post

# test we get a list of accounts when calling #all
def test_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    assert repository.all() == [
        Account(1, 'diana_cavendish@lunanova.com', 'dcavendish'),
        Account(2, 'kagari.akko@lunanova.com', 'ShinyChariotFan1'),
        Account(3, 'manbavaran@lunanova.com', 'kinoko')
    ]

# test we find specified account based on provided id when calling #find
def test_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    assert repository.find(2) == Account(2, 'kagari.akko@lunanova.com', 'ShinyChariotFan1')

# test that we can add a new account to the database when calling #create
def test_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    repository.create(Account(None, 'edelgard_von_hresvelg@garregmach.net', 'Emperor'))
    assert repository.all() == [
        Account(1, 'diana_cavendish@lunanova.com', 'dcavendish'),
        Account(2, 'kagari.akko@lunanova.com', 'ShinyChariotFan1'),
        Account(3, 'manbavaran@lunanova.com', 'kinoko'),
        Account(4, 'edelgard_von_hresvelg@garregmach.net', 'Emperor')
    ]

# test that given a specific id, record is deleted from database when calling #delete
def test_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    repository.delete(2)
    assert repository.all() == [
        Account(1, 'diana_cavendish@lunanova.com', 'dcavendish'),
        Account(3, 'manbavaran@lunanova.com', 'kinoko')
    ]

# test that given an account, we get the account and its associated posts when calling #find_with_posts
def test_find_with_posts(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    assert repository.find_with_posts(2) == Account(2, 'kagari.akko@lunanova.com', 'ShinyChariotFan1', [
    Post(2, 'Shiny Chariot at Luna Nova', 'I have been following in the footsteps of Chariot while at Luna Nova and I have discovered many things!', 4, 2),
    Post(5, 'How to unstransform oneself', 'Please help.', 5, 2)
    ])
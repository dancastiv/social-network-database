from lib.post_repository import PostRepository
from lib.post import Post

# test we get a list of posts when calling #all
def test_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    assert repository.all() == [
    Post(1, 'Samhain Festival', 'This is a reminder to the student body to carry their weight during the festival.', 2552, 1),
    Post(2, 'Shiny Chariot at Luna Nova', 'I have been following in the footsteps of Chariot while at Luna Nova and I have discovered many things!', 4, 2),
    Post(3, 'Importance of Schoolwork', 'Please remember that we are at school to learn, not follow terrible role models.', 3452, 1),
    Post(4, 'Looking for mushrooms', 'I am looking for mushrooms. Will pay for information.', 632, 3),
    Post(5, 'How to unstransform oneself', 'Please help.', 5, 2)
        ]
    
# test we find specified account based on provided id when calling #find
def test_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    assert repository.find(4) == Post(4, 'Looking for mushrooms', 'I am looking for mushrooms. Will pay for information.', 632, 3)

# test we can add new posts to database when calling #create
def test_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'Still trying to figure out how to untransform', 'This is not funny, I need help!', 6, 2))
    assert repository.all() == [
    Post(1, 'Samhain Festival', 'This is a reminder to the student body to carry their weight during the festival.', 2552, 1),
    Post(2, 'Shiny Chariot at Luna Nova', 'I have been following in the footsteps of Chariot while at Luna Nova and I have discovered many things!', 4, 2),
    Post(3, 'Importance of Schoolwork', 'Please remember that we are at school to learn, not follow terrible role models.', 3452, 1),
    Post(4, 'Looking for mushrooms', 'I am looking for mushrooms. Will pay for information.', 632, 3),
    Post(5, 'How to unstransform oneself', 'Please help.', 5, 2),
    Post(6, 'Still trying to figure out how to untransform', 'This is not funny, I need help!', 6, 2)
    ]

# test that given a specific id, we can delete record from database when calling #delete
def test_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.delete(3)
    assert repository.all() == [
    Post(1, 'Samhain Festival', 'This is a reminder to the student body to carry their weight during the festival.', 2552, 1),
    Post(2, 'Shiny Chariot at Luna Nova', 'I have been following in the footsteps of Chariot while at Luna Nova and I have discovered many things!', 4, 2),
    Post(4, 'Looking for mushrooms', 'I am looking for mushrooms. Will pay for information.', 632, 3),
    Post(5, 'How to unstransform oneself', 'Please help.', 5, 2)
        ]
    
# test that given a specific account_id, all their posts are returned when calling #all_posts
def test_all_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    assert repository.all_posts(1) == [
    Post(1, 'Samhain Festival', 'This is a reminder to the student body to carry their weight during the festival.', 2552, 1),
    Post(3, 'Importance of Schoolwork', 'Please remember that we are at school to learn, not follow terrible role models.', 3452, 1)
        ]
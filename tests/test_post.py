from lib.post import Post

# test account constructs with username and email_address
def test_post_constructs():
    post = Post(1, 'A title', 'The contents.', 5, 1)
    assert post.id == 1
    assert post.title == 'A title'
    assert post.content == 'The contents.'
    assert post.views == 5
    assert post.account_id == 1

# test two identical accounts are equal
def test_accounts_are_equal():
    post1 = Post(1, 'A title', 'The contents.', 5, 1)
    post2 = Post(1, 'A title', 'The contents.', 5, 1)
    assert post1 == post2
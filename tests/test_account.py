from lib.account import Account

# test account constructs with username and email_address
def test_account_constructs():
    account = Account(1, 'tachibana_wato@gmail.com', 'watosan')
    assert account.email_address == 'tachibana_wato@gmail.com'
    assert account.username == 'watosan'

# test two identical accounts are equal
def test_accounts_are_equal():
    account1 = Account(1, 'tachibana_wato@gmail.com', 'watosan')
    account2 = Account(1, 'tachibana_wato@gmail.com', 'watosan')
    assert account1 == account2
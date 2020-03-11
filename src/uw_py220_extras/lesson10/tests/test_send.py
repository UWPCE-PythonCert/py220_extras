from mailing_list import send


def test_send():
    assert send.send_message("xxx", "yyy") == True

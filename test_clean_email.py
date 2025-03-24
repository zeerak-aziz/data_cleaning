import pytest
from clean_email import clean_email


# PyTest unit tests
def test_clean_email_normal():
    text = "hello, you can contact me at zeerak.aziz@example.com"
    assert clean_email(text) == "hello, you can contact me at ****"


def test_clean_email_multiple():
    text = "emails: user1@domain.com, user2@example.org"
    assert clean_email(text) == "emails: ****, ****"


def test_clean_email_no_email():
    text = "no email here!"
    assert clean_email(text) == "no email here!"


def test_clean_email_edge():
    text = "email: admin@something"
    assert clean_email(text) == "email: ****"


def test_clean_email_mixed():
    text = "contact at john.doe@example.com for info, or visit example.com"
    assert clean_email(text) == "contact at **** for info, or visit example.com"


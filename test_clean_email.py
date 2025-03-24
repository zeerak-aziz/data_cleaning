import pytest
from clean_email import clean_email


# PyTest unit tests
def test_clean_email_masks_standard_email_format():
    text = "hello, you can contact me at zeerak.aziz@example.com"
    assert clean_email(text) == "hello, you can contact me at ****"


def test_clean_email_masks_multiple_emails_in_text():
    text = "emails: user1@domain.com, user2@example.org"
    assert clean_email(text) == "emails: ****, ****"


def test_clean_email_retains_text_with_no_emails():
    text = "no email here!"
    assert clean_email(text) == "no email here!"


def test_clean_email_invalid_email_format():
    text = "email: admin@something"
    assert clean_email(text) == "email: ****"


def test_clean_email_retains_website_name_and_masks_standard_email():
    text = "contact at john.doe@example.com for info, or visit example.com"
    assert clean_email(text) == "contact at **** for info, or visit example.com"


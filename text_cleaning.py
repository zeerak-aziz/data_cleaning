import re

def clean_email(text):
    """
    takes a string and removes any email addresses, replaces with '****'.
    :param text: The input text containing potential email addresses.
    :return: The text with email addresses obscured.
    """
    # basic regex: Regex pattern that matches most email formats, it does not reject john@doe..com
    # email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 

    # Advanced regex: this should disallow leading and trailing dots in most places
    email_pattern = r'[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'


    cleaned_text = re.sub(email_pattern, '****', text)
    return cleaned_text
    

# PyTest unit tests
def test_clean_email_normal():
    text = "hello, you can contact me at zeerak.aziz@example.com"
    assert clean_email(text) == "Hello, you can contact me at ****"


def test_clean_email_multiple():
    text = "emails: user1@domain.com, user2@example.org"
    assert clean_email(text) == "Emails: ****, ****"


def test_clean_email_no_email():
    text = "no email here!"
    assert clean_email(text) == "No email here!"


def test_clean_email_edge():
    text = "email: admin@localhost"
    assert clean_email(text) == "Email: ****"


def test_clean_email_mixed():
    text = "contact at john.doe@example.com for info, or visit example.com"
    assert clean_email(text) == "Contact at **** for info, or visit example.com"


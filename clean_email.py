import re

def clean_email(text):
    """
    takes a string and removes any email addresses, replaces with '****'.
    :param text: The input text containing potential email addresses.
    :return: The text with email addresses obscured.
    """
    # basic regex: Regex pattern that matches most email formats
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?' 

    # Advanced regex: this should disallow leading and trailing dots in most places
    # not working - return to basic
    # email_pattern = r'[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
    
    cleaned_text = re.sub(email_pattern, '****', text)
    return cleaned_text
    
if __name__ == "__main__":
    sample_text = "Contact me at john@doe..com or jane.doe@domain.com."
    print("Original text:", sample_text)
    print("Cleaned text:", clean_email(sample_text))


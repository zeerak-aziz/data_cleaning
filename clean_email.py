import re

def clean_email(text: str) -> str:
    """
    takes a string and removes any email addresses, replaces with '****'
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?' 
    
    cleaned_text = re.sub(email_pattern, '****', text)
    return cleaned_text
    
if __name__ == "__main__":
    sample_text = "Contact me at john@doe..com or jane.doe@domain.com."
    print("Original text:", sample_text)
    print("Cleaned text:", clean_email(sample_text))



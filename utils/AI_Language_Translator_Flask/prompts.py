def validate_input(text):
    """
    Check if the input text is empty.
    """
    if not text or text.strip() == "":
        return False
    return True


def clean_text(text):
    """
    Remove extra spaces from the text.
    """
    return text.strip()
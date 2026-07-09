import re
from unidecode import unidecode


def clean_text(text: str) -> str:
    """
    Clean extracted text before NLP processing.
    """

    # Convert unicode characters to ASCII
    text = unidecode(text)

    # Lowercase
    text = text.lower()

    # Remove newlines and tabs
    text = re.sub(r"[\n\t\r]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove punctuation except +, #, .
    text = re.sub(r"[^\w\s\+#\.]", " ", text)

    # Remove multiple spaces again
    text = re.sub(r"\s+", " ", text)

    return text.strip() 
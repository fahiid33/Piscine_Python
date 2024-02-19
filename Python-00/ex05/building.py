
"""Count the number of upper-case letters, lower-case letters,
punctuation marks, digits, and spaces in a given text.

Usage:
    python building.py "text"

If no text is provided as a command-line argument, the user
will be prompted to enter a string.
"""

import sys
import string


def count_characters(text):
    """
    Count the number of upper-case letters, lower-case letters,
    punctuation marks, digits, and spaces in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        None
    """
    if text is None or text == "":
        print("What is the text to count?")
        text = sys.stdin.readline()

    upper_cnt = 0
    lower_cnt = 0
    punctuation_cnt = 0
    digit_cnt = 0
    space_cnt = 0

    for char in text:
        if char.isupper():
            upper_cnt += 1
        elif char.islower():
            lower_cnt += 1
        elif char in string.punctuation:
            punctuation_cnt += 1
        elif char.isdigit():
            digit_cnt += 1
        elif char.isspace():
            space_cnt += 1

    total_count = (
        upper_cnt + lower_cnt + punctuation_cnt + digit_cnt + space_cnt
    )

    print(f"The text contains {total_count} characters:")
    print(f"{upper_cnt} upper letters")
    print(f"{lower_cnt} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{digit_cnt} digits")
    print(f"{space_cnt} spaces")


if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "Exactly one argument is required"
        count_characters(sys.argv[1] if len(sys.argv) > 1 else None)
    except AssertionError as e:
        print("AssertionError:", e)

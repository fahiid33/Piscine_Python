import sys
from ft_filter import ft_filter


def  filterstring(sentence, length):
    """
    Filters words from the given sentence based on their length.

    Args:
        sentence (str): The input sentence containing words separated by spaces.
        length (int): The minimum length of words to include in the result.

    Returns:
        list: A list of words from the sentence that have a length greater than the given length.
    """
    words = sentence.split()
    # filtered_words = [word for word in words if (lambda word: len(word) > length)(word)]
    # return filtered_words
    return list(ft_filter(lambda word: len(word) > length, words))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "Exactly two arguments are required"
        sentence = sys.argv[1]
        length = int(sys.argv[2])
        assert isinstance(sentence, str) and isinstance(length, int), "Invalid argument types"
        filtered_words = filterstring(sentence, length)
        print(filtered_words)
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: ","Invalid argument types")

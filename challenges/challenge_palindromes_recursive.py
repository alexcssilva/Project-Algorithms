def is_palindrome_recursive(word, low_index, high_index):
    try:
        if low_index == high_index or low_index > high_index:
            return True
    except TypeError:
        return None
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

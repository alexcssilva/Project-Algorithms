def is_palindrome_iterative(word):
    if str(word) == str(word)[::-1] and word not in '':
        return True
    else:
        return False

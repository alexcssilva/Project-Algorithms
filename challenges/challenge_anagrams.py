def is_anagram(first_string, second_string):
    first_word = first_string.lower()
    second_word = second_string.lower()
    for row in first_word:
        if row in second_word:
            second_word = second_word.replace(row, "", 1)
        else:
            return False
    return len(second_word) == 0

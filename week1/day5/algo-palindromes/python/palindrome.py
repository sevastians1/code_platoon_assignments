def palindrome(word):
    word = str(word)

    new_str = ''

    for char in (word):
        if char.isalpha() or char.isnumeric():
            new_str += char.lower()
    

    if new_str == new_str[::-1]:
        return True

    return False
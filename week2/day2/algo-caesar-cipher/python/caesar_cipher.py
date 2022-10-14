def caesar_cipher(string, shift_amount):
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    capital_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result_arr = []

    for letter in string:
        if letter.isalpha() and letter.lower() == letter:
            current_index = lower_alpha.index(letter)
            if current_index + shift_amount > 26:
                updated_index = (current_index + shift_amount) - 26
            else:
                updated_index = current_index + shift_amount
            result_arr.append(lower_alpha[updated_index])

        elif letter.isalpha() and letter.upper() == letter:
            current_index = capital_alpha.index(letter)
            if current_index + shift_amount > 26:
                updated_index = (current_index + shift_amount) - 26
            else:
                updated_index = current_index + shift_amount
            result_arr.append(capital_alpha[updated_index])

        else:
            result_arr.append(letter)

    return ''.join(result_arr)
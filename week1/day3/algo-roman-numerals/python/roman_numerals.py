def to_roman(num):
    roman_num_arr = {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1,
    }

    result = ''

    # print(roman_num_arr[0])

    while num > 0:
        for key in roman_num_arr:

            if num >= roman_num_arr[key]:
                result += key
                num -= roman_num_arr[key]

    return result
    
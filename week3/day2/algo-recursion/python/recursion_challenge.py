def factorial(x):

	if x == 0:
		return 1
	

	return x * factorial(x - 1)

def palindrome(string):
	pass

def bottles(num):
	
	if num == 0:
		return "No bottles left"

	print(f"{num} bottles of beer on the wall")

	return bottles(num - 1)

def roman_num(num):
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

	str = ''

	for key in roman_num_arr:
		if num >= roman_num_arr[key]:
			str += key
			return roman_num(num - roman_num_arr[key])


	if num == 0:
		return str
# Don't forget to run your tests!

def is_character_match(string1, string2):
	letter_count = {}

	string1 = string1.lower()
	string2 = string2.lower()

	string1 = string1.replace(' ', '')
	string2 = string2.replace(' ', '')

	for char in string1:
		if char in letter_count:
			letter_count[char] += 1
		else:
			letter_count[char] = 1

	for char in string2:
		if char in letter_count:
			letter_count[char] -= 1
		else:
			return False

	# print(letter_count)

	for key in letter_count:
		if letter_count[key] > 0:
			return False
	
	return True

	# print(letter_count)
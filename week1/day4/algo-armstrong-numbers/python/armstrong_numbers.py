def find_armstrong_numbers(numbers):

	result = []

	for num in numbers:
		length = len(str(num))
		
		sum = 0

		
		for single_digit in str(num):
			sum += int(single_digit) ** length

		if sum == num:
			result.append(num)
			# print(num)

	# print(result)
			
	return result
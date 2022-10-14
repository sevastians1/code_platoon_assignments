def char_count(str):

  str = str.replace(' ', '')

  count_dict = {}
  count_arr = []

  for letter in str:
    
    if letter in count_dict:
      count_dict[letter] += 1

    else:
      count_dict[letter] = 1

  for value in enumerate(count_dict):
    count_arr.append([value, count_dict[value]])


  sorted_arr = sorted(sorted(count_arr, key=lambda letter : letter), key=lambda letter : letter[1], reverse=True)
  # print(sorted_arr)

  return sorted_arr
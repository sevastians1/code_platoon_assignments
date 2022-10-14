
def translate(word_or_phrase):

  if ' ' in word_or_phrase:
    str_arr = word_or_phrase.split(' ')
  else:
    return single_word(word_or_phrase)

  # print(str_arr)

  str_arr_result = []
  for word in str_arr:
    str_arr_result.append(single_word(word))

  # print(' '.join(str_arr_result))
  return ' '.join(str_arr_result)


def single_word(word):
  vowel = 'aeiou'
  str_arr = []
  

  if ' ' in word:
    str_arr = word.split(' ')
    

  if str_arr == []:
    if word[0].upper() == word[0]:
      cap_first_letter = True

    for i in range (len(word)):
      if word[0].lower() not in vowel:
        if word[0] == 'q' and word[1] == 'u':
          word = word[2:] + word[:2].lower()
        else:
          word = word[1:] + word[0].lower()
      elif word[0].lower() in vowel:
        word = word + 'ay'
        break

    try:
      if cap_first_letter:
        return word.capitalize()
    
    except:
        return word.lower()
import random


class BoggleBoard:
  
  def __init__(self):
    self.board = [[' '] * 4 for row in range(4)]
    self.dices = [
      ['A','A','E','E','G','N'],
      ['E','L','R','T','T','Y'],
      ['A','O','O','T','T','W'],
      ['A','B','B','J','O','O'],
      ['E','H','R','T','V','W'],
      ['C','I','M','O','T','U'],
      ['D','I','S','T','T','Y'],
      ['E','I','O','S','S','T'],
      ['D','E','L','R','V','Y'],
      ['A','C','H','O','P','S'],
      ['H','I','M','N','Q','U'],
      ['E','E','I','N','S','U'],
      ['E','E','G','H','N','W'],
      ['A','F','F','K','P','S'],
      ['H','L','N','N','R','Z'],
      ['D','E','I','L','R','X'],
    ]

  
  def display_board(self):
    for row in self.board:
      print(row)


  def shake(self, to_shake):

    random_sixteen = []

    for i in range(16):
      # print(self.dices[i])

      random_num = random.randint(0,len(self.dices[i]) - 1)
      # print(random_num)
      letter_to_use = self.dices[i][random_num]
      
      if letter_to_use == 'Q':
        random_sixteen.append(letter_to_use + 'u')
      else:
        random_sixteen.append(letter_to_use)

      del self.dices[i][random_num]

      # print(self.dices[i])

    if to_shake == 'Shake!':
      for i in range(4):
        for n in range(4):
          rand_num = random.randint(0, len(random_sixteen) - 1)
          self.board[i][n] = random_sixteen[random.randint(0, rand_num)]
          del random_sixteen[rand_num]
    # print(self.board)
    print(random_sixteen)

test = BoggleBoard()
print(test.display_board())
print(test.shake('Shake!'))
print(test.display_board())
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
            # print(random_sixteen)

      def inclue_word(self, word):
            
            for col in range(len(self.board)):
                  col_arr = []
                  for row in range(len(self.board)):
                        col_arr.append(self.board[row][col])

                  if ''.join(col_arr) == word or ''.join(col_arr[::-1]) == word:
                        return True

            for row in self.board:
            
                  # print(self.board[row][::-1])
                  if ''.join(row) == word or ''.join(row[::-1]) == word:
                        return True

            return False


def run_boggle(run=True):
      game = BoggleBoard()
      
      i = 0

      while i < 6:
            game.shake('Shake!')
            # game.display_board()
            game.inclue_word('SAND')

            if game.inclue_word('SAND') == True:
                  return True

            i += 1


# if you run this it will take a minute
# ran it 100000 to get a good sample size to calculate the percentage that the inputed word will be on the board
# it is about a 0.01% rate
count = 0
i = 0
while i < 100000:
      run_boggle()
      if run_boggle() == True:
            count += 1
      i += 1

print(count)




# test = BoggleBoard()
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())
# test.shake('Shake!')
# print(test.inclue_word('FOUR'))
# # print(test.display_board())

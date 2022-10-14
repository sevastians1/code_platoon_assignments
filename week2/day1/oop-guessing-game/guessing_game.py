

class GuessingGame:

    def __init__(self, guess):
        self.guess = guess

    def user_guess(self, user_guess):

        if user_guess > self.guess:
            return 'high'
        elif user_guess < self.guess:
            return 'low'
        return 'correct'


    def solved(self, user_guess):
        if self.guess == user_guess:
            return True

        return False

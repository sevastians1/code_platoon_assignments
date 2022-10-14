# Your PremiumUser class goes here
from User import User


class PremiumUser(User):
    def __init__(self, name):
        parent_instance = super()
        parent_instance.__init__(name)
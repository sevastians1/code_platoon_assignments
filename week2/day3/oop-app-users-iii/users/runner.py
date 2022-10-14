# Import and create your users here
from FreeUser import FreeUser
from User import User
# from users.PremiumUser import PremiumUser


sam = FreeUser('sam')
print(vars(sam))

sam.create_post(0, 'title1', 'description1')
print(sam.all_posts)

sam.create_post(1, 'title2', 'description2')
# print(sam._allowed)
print(sam.create_post(2, 'title3', 'description3'))
# print(sam._allowed)
sam.create_post(3, 'title4', 'description4')

print(User.print_post('sam'))

sam.delete_post(1)

print(User.print_post('sam'))

sam.create_post(3, 'title3', 'description3')
print(User.print_post('sam'))
print(User.all_posts)
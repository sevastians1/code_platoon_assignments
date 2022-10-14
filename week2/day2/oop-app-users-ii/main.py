from User import User

sam = User('sam')

sam.create_post(0, 'title', 'description')
sam.create_post(1, 'title2', 'description')
sam.create_post(2, 'title3', 'description')
sam.create_post(3, 'title4', 'description')

dan = User('dan')

dan.create_post(4, 'title', 'description')
dan.create_post(5, 'title2', 'description')
dan.create_post(6, 'title3', 'description')
dan.create_post(7, 'title4', 'description')


# sam.delete_post(1)


# print(User.all_posts)

print(User.print_post('sam'))

print(User.all_posts)
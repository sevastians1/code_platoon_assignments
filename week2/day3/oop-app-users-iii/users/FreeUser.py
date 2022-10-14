
from User import User


class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)
        # self._allowed = True
        self._limit = 0

    def create_post(self, id, title, description):
        self._limit = len(User.all_posts)

        if self._limit < 2:
            User.all_posts.append({'id':id, 'name':self.name, 'post_title': title, 'post_description':description})
            # self._limit += 1
        else:
            return 'You have reached the number of posts you can create with a free account.'
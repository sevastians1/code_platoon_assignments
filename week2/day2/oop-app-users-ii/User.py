# your improved User class goes here


class User:
    all_posts = []

    def __init__(self, name):
        self.name = name

    def create_post(self, id, title, description):
        
        User.all_posts.append({'id':id, 'name':self.name, 'post_title': title, 'post_description':description})

    def delete_post(self, id):
        for dict in User.all_posts:
            if dict.get('id') == id:
                User.all_posts.remove(dict)

    @staticmethod
    def print_post(name):
        users_post = []
        for post in User.all_posts:
            if post['name'] == name:
                users_post.append(post)

        return users_post


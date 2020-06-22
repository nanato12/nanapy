from .object import User, Post
from .service import Service

class Nana:
    def __init__(self, email=None, password=None):
        self.service = Service(email, password)
        self.profile = User(self.service.get_my_info())

    def get_user(self, user_id):
        return User(self.service.get_user(user_id))

    def get_post(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        return Post(self.service.get_post(post_id))

    def follow(self, user_id):
        self.service.follow_user(user_id)

    def unfollow(self, user_id):
        self.service.unfollow_user(user_id)

    def play(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self.service.post_play(post_id)

    def applause(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self.service.post_applause(post_id)

    def unapplause(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self.service.post_unapplause(post_id)

    def comment(self, post_id, comment, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self.service.post_comment(post_id, comment)

    def logout(self):
        self.service.logout()

    @property
    def email(self):
        return self.service.email

    @property
    def password(self):
        return self.service.password

    @property
    def token(self):
        return self.service.token

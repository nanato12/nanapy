from .object import User, Post, Community
from .service import Service
from .callback import log

def check(func):
    def check_login(*args, **kwargs):
        if args[0].is_login:
            return func(*args, **kwargs)
        else:
            raise Exception('You are not logged in.')
    return check_login

class Nana:

    is_login = False

    def __init__(self, email=None, password=None, token=None):
        if token:
            self._service = Service(token=token)
            login_type = 'Token'
        elif email and password:
            self._service = Service(email, password)
            login_type = 'Email'
        else:
            self._service = Service(email, password)
            login_type = 'Create'
            self.log(f'email: {self.email}, password: {self.password}')
        self.profile = User(self._service.get_my_info())
        self.is_login = True
        self.log(
            '[{user_name}] : {login_type} Login Success'.format(
                user_name=self.profile.screen_name,
                login_type=login_type
            )
        )
        self.log(f'user_id: {self.profile.user_id}')
        self.log(f'token: {self._service.token}')

    @check
    def get_user(self, user_id):
        return User(self._service.get_user(user_id))

    @check
    def get_post(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        return Post(self._service.get_post(post_id))

    @check
    def get_community(self, community_id):
        return Community(self._service.get_community(community_id))

    @check
    def follow_user(self, user_id):
        self._service.follow_user(user_id)

    @check
    def unfollow_user(self, user_id):
        self._service.unfollow_user(user_id)

    @check
    def play_post(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self._service.post_play(post_id)

    @check
    def applause_post(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self._service.post_applause(post_id)

    @check
    def unapplause_post(self, post_id, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self._service.post_unapplause(post_id)

    @check
    def comment_post(self, post_id, comment, is_hex=True):
        post_id = int(post_id, 16) if is_hex else post_id
        self._service.post_comment(post_id, comment)

    @check
    def join_community(self, community_id):
        self._service.join_community(community_id)

    @check
    def leave_community(self, community_id):
        self._service.leave_community(community_id)

    @check
    def logout(self):
        self._service.logout()
        self.is_login = False

    def log(self, message):
        log(message)

    @property
    def email(self):
        return self._service.email

    @property
    def password(self):
        return self._service.password

    @property
    def token(self):
        return self._service.token

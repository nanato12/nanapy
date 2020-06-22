import requests

from .func import Func
from .config import Config
from .error import (
    LoginError,
    LogoutError,
    SignupError,
    NotFoundUser,
    NotFoundPost,
    FollowError,
    PlayError,
    ApplauseError,
    CommentError
)

class Service(Config):

    is_login = False
    email = None
    password = None
    token = None
    device_id = None
    appsflyer_id = None
    session = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.initialize_session()

        if self.email is not None and self.password is not None:
            self.login()
        else:
            self.create_account()

    def initialize_session(self):
        self.session = requests.session()
        self.device_id = Func.generate_device_id()
        self.appsflyer_id = Func.generate_appsflyer_id()
        self.HEADERS['x-device-identifier'] = self.device_id
        self.HEADERS['x-appsflyer-identifier'] = self.appsflyer_id

    def login(self):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.LOGIN_PATH
        params = {
            'device_id': self.device_id,
            'email': self.email,
            'password': self.password,
            'type': 'nana'
        }
        res = self.session.post(
            url=url,
            headers=self.HEADERS,
            json=params
        )
        resource = res.json()
        if res.status_code == 200:
            self.is_login = True
        else:
            raise LoginError(resource['data']['message'])
        self.token = resource['data']['token']
        self.HEADERS['authorization'] = f'token {self.token}'

    def create_account(self):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.SIGNUP_PATH
        params = {
            'device_id': self.device_id,
            'screen_name': Func.random_string(6)
        }
        res = self.session.post(
            url=url,
            headers=self.HEADERS,
            json=params
        )
        resource = res.json()
        if res.status_code == 200:
            self.is_login = True
        else:
            raise SignupError(resource['data']['message'])
        self.token = resource['data']['token']
        self.HEADERS['authorization'] = f'token {self.token}'

    def get_my_info(self):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + self.MYPAGE_PATH
        res = self.session.get(
            url=url,
            headers=self.HEADERS
        )
        return res.json()

    def get_user(self, user_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.USER_PATH.format(user_id=user_id)
        res = self.session.get(
            url=url,
            headers=self.HEADERS
        )
        if res.status_code == 404:
            raise NotFoundUser(f'{user_id} is not found.')
        return res.json()

    def get_post(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_PATH.format(post_id=post_id)
        res = self.session.get(
            url=url,
            headers=self.HEADERS
        )
        if res.status_code == 404:
            raise NotFoundUser(f'{post_id} is not found.')
        return res.json()

    def follow_user(self, user_id):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + \
            self.USER_FOLLOW_PATH.format(user_id=user_id)

        res = self.session.post(
            url=url,
            headers=self.HEADERS
        )
        resource = res.json()
        if res.status_code != 200:
            raise FollowError('failed.')
        return resource

    def unfollow_user(self, user_id):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + \
            self.USER_FOLLOW_PATH.format(user_id=user_id)

        res = self.session.delete(
            url=url,
            headers=self.HEADERS
        )
        resource = res.json()
        if res.status_code != 200:
            raise FollowError('failed.')
        return resource

    def post_play(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_PLAY_PATH.format(post_id=post_id)

        res = self.session.post(
            url=url,
            headers=self.HEADERS
        )
        if res.status_code != 200:
            raise PlayError('failed.')

    def post_applause(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_APPLAUSE_PATH.format(post_id=post_id)

        res = self.session.post(
            url=url,
            headers=self.HEADERS
        )
        if res.status_code != 200:
            raise ApplauseError('failed.')

    def post_unapplause(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_APPLAUSE_PATH.format(post_id=post_id)

        res = self.session.delete(
            url=url,
            headers=self.HEADERS
        )
        if res.status_code != 200:
            raise ApplauseError('failed.')

    def post_comment(self, post_id, comment):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_COMMENT_PATH.format(post_id=post_id)

        res = self.session.post(
            url=url,
            headers=self.HEADERS,
            json={'body': comment}
        )
        if res.status_code != 200:
            raise CommentError('failed.')

    def logout(self):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.LOGOUT_PATH

        res = self.session.post(
            url=url,
            headers=self.HEADERS
        )
        resource = res.json()
        if res.status_code != 200:
            raise LogoutError('failed.')

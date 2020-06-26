import requests

from requests.exceptions import Timeout

from .func import Func
from .config import Config
from .error import (
    LoginError,
    LogoutError,
    SignupError,
    NotFoundUser,
    NotFoundPost,
    NotFoundCommunity,
    NotFoundMyData,
    FollowError,
    PlayError,
    ApplauseError,
    CommentError,
    CommunityJoinError,
    CommunityLeaveError,
    NanapyError
)

class Service(Config):

    email = None
    password = None
    token = None
    proxy = None
    device_id = None
    appsflyer_id = None
    session = None

    def __init__(self, email, password, name, token, create, proxy):
        self.initialize_session()

        if proxy:
            self.proxy = {'https': proxy}

        self.email = email
        self.password = password

        if create:
            self.create_account(name=name)
        elif token:
            self.set_token(token)
        elif email and password:
            self.login()
        else:
            raise NanapyError(
                '\n\nCreate or Login failed.\n' + \
                'If you want create account: Nana(create=True)\n' + \
                'If you want login: Nana(email, password) or ' + \
                'Nana(token=\'XXXXXXXXXX\')\n'
            )

    def initialize_session(self):
        self.session = requests.session()
        self.device_id = Func.generate_device_id()
        self.appsflyer_id = Func.generate_appsflyer_id()
        self.HEADERS['x-device-identifier'] = self.device_id
        self.HEADERS['x-appsflyer-identifier'] = self.appsflyer_id

    def get_request(self, url):
        try:
            return self.session.get(
                url=url,
                headers=self.HEADERS,
                proxies=self.proxy,
                timeout=5.0
            )
        except Timeout:
            raise TimeoutError('connection timeout.')

    def post_request(self, url, json=None):
        try:
            return self.session.post(
                url=url,
                headers=self.HEADERS,
                json=json,
                proxies=self.proxy,
                timeout=5.0
            )
        except Timeout:
            raise TimeoutError('connection timeout.')

    def delete_request(self, url):
        try:
            return self.session.delete(
                url=url,
                headers=self.HEADERS,
                proxies=self.proxy,
                timeout=5.0
            )
        except Timeout:
            raise TimeoutError('connection timeout.')

    def login(self):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.LOGIN_PATH
        params = {
            'device_id': self.device_id,
            'email': self.email,
            'password': self.password,
            'type': 'nana'
        }

        res = self.post_request(url, json=params)
        resource = res.json()
        if res.status_code != 200:
            raise LoginError(resource['data']['message'])
        self.set_token(resource['data']['token'])

    def create_account(self, name=None):
        if name is None:
            name = Func.random_string(6)
        if self.email is None:
            self.email = f'{name}@email.com'
        if self.password is None:
            self.password = Func.random_hex(6)

        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.SIGNUP_PATH
        params = {
            'device_id': self.device_id,
            'screen_name': name,
            'email': self.email,
            'password': self.password,
            'type': 'nana'
        }

        res = self.post_request(url, json=params)
        resource = res.json()
        if res.status_code != 200:
            raise SignupError(resource['data']['message'])
        self.set_token(resource['data']['token'])

    def set_token(self, token):
        self.token = token
        self.HEADERS['authorization'] = f'token {self.token}'

    def get_my_info(self):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + self.MYPAGE_PATH

        res = self.get_request(url)
        resource = res.json()
        if res.status_code != 200:
            raise NotFoundMyData(resource['data']['message'])
        return resource

    def get_user(self, user_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.USER_PATH.format(user_id=user_id)

        res = self.get_request(url)
        if res.status_code != 200:
            raise NotFoundUser(f'{user_id} is not found.')
        return res.json()

    def get_post(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_PATH.format(post_id=post_id)

        res = self.get_request(url)
        if res.status_code != 200:
            raise NotFoundUser(f'{post_id} is not found.')
        return res.json()

    def get_community(self, community_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.COMMUNITY_PATH.format(community_id=community_id)

        res = self.get_request(url)
        if res.status_code != 200:
            raise NotFoundCommunity(f'{community_id} is not found.')
        return res.json()

    def follow_user(self, user_id):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + \
            self.USER_FOLLOW_PATH.format(user_id=user_id)

        res = self.post_request(url)
        if res.status_code != 200:
            raise FollowError('failed.')
        return res.json()

    def unfollow_user(self, user_id):
        url = self.HOST_DOMAIN + self.LATEST_VERSION + \
            self.USER_FOLLOW_PATH.format(user_id=user_id)

        res = self.delete_request(url)
        resource = res.json()
        if res.status_code != 200:
            raise FollowError('failed.')
        return resource

    def post_play(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_PLAY_PATH.format(post_id=post_id)

        res = self.post_request(url)
        if res.status_code != 200:
            raise PlayError('failed.')

    def post_applause(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_APPLAUSE_PATH.format(post_id=post_id)

        res = self.post_request(url)
        if res.status_code != 200:
            raise ApplauseError('failed.')

    def post_unapplause(self, post_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_APPLAUSE_PATH.format(post_id=post_id)

        res = self.delete_request(url)
        if res.status_code != 200:
            raise ApplauseError('failed.')

    def post_comment(self, post_id, comment):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.POST_COMMENT_PATH.format(post_id=post_id)

        res = self.post_request(url, json={'body': comment})
        if res.status_code != 200:
            raise CommentError('failed.')

    def join_community(self, community_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.COMMUNITY_JOIN_PATH.format(community_id=community_id)

        res = self.post_request(url)
        if res.status_code != 200:
            raise CommunityJoinError('failed.')

    def leave_community(self, community_id):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + \
            self.COMMUNITY_JOIN_PATH.format(community_id=community_id)

        res = self.delete_request(url)
        if res.status_code != 200:
            raise CommunityLeaveError('failed.')

    def logout(self):
        url = self.HOST_DOMAIN + self.LEGACY_VERSION + self.LOGOUT_PATH

        res = self.post_request(url)
        resource = res.json()
        if res.status_code != 200:
            raise LogoutError('failed.')

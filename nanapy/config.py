class Config:
    HOST_DOMAIN = 'https://jackson.nana-music.com'

    LATEST_VERSION = '/v2.1'
    LEGACY_VERSION = '/v2'

    LOGIN_PATH = '/login'
    LOGOUT_PATH = '/logout'
    SIGNUP_PATH = '/signup'
    MYPAGE_PATH = '/my_page'
    USER_PATH = '/users/{user_id}'
    USER_FOLLOW_PATH = USER_PATH + '/follow'
    POST_PATH = '/posts/{post_id}'
    POST_PLAY_PATH = POST_PATH + '/play'
    POST_APPLAUSE_PATH = POST_PATH + '/applause'
    POST_COMMENT_PATH = POST_PATH + '/comments'

    OS_VERSION = '13.3.1'
    APP_VERSION = '3.10.2'

    HEADERS = {
        'accept': '*/*',
        'content-type': 'application/json',
        'x-ios-device': 'iPhone9,1',
        'x-ios-version': OS_VERSION,
        'x-app-version': APP_VERSION,
        'accept-language': 'ja-JP;q=1.0, en-US;q=0.9',
        'accept-encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
        'user-agent': f'nana/{APP_VERSION} (iPhone; iOS {OS_VERSION}; Scale/2.00)'
    }

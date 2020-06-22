class User:

    ad_server = None
    android_purchase_expires_date = None
    applause_count = None
    birthday = None
    community_count = None
    country = None
    cover_pic_url = None
    facebook_url = None
    firebase_properties = None
    follower_count = None
    following_count = None
    gender = None
    ios_purchase_expires_date = None
    is_blocked = None
    is_blocking = None
    is_favorite = None
    is_follower = None
    is_following = None
    is_mute = None
    is_official = None
    is_premium = None
    is_premium_by_ticket = None
    pic_url = None
    pic_url_large = None
    pic_url_medium = None
    pinned_playlist = None
    pinned_post = None
    playlist_count = None
    premium_ticket_expires_date = None
    profile = None
    profile_url = None
    screen_name = None
    sound_count = None
    trial_premium_functions = None
    twitter_url = None
    user_id = None

    def __init__(self, user_data):
        self.__dict__.update(user_data)

    def __str__(self):
        return 'User({})'.format(
            ', '.join(
                [f'{key}={value}' for key, value in self.__dict__.items()]
            )
        )

class Post:

    def __init__(self, post_data):
        self.__dict__.update(post_data)

    def __str__(self):
        return 'Post({})'.format(
            ', '.join(
                [f'{key}={value}' for key, value in self.__dict__.items()]
            )
        )

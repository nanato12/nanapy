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

    post_id = None
    created_at = None
    user = None
    part_id = None
    caption = None
    artist = None
    title = None
    duration = None
    sound_url = None
    is_collabo_waiting = None
    key = None
    play_count = None
    applause_count = None
    comment_count = None
    collabo_count = None
    collabos = None
    player_url = None
    private = None
    single_track_url = None
    is_mixed = None
    is_collabo_later = None
    is_applauded = None
    is_reposted = None
    comments = None
    overdub_count = None
    genre = None
    music_key = None
    acc = None
    ogp_url = None
    language = None
    acc_post = None

    def __init__(self, post_data):
        self.__dict__.update(post_data)
        self.user = User(self.user)
        self.comments = [Comment(comment) for comment in self.comments]

    def __str__(self):
        return 'Post({})'.format(
            ', '.join(
                [f'{key}={value}' for key, value in self.__dict__.items()]
            )
        )

class Comment:

    comment_id = None
    created_at = None
    body = None
    user = None
    reply_to = None

    def __init__(self, comment_data):
        self.__dict__.update(comment_data)
        self.user = User(self.user)

    def __str__(self):
        return 'Comment({})'.format(
            ', '.join(
                [f'{key}={value}' for key, value in self.__dict__.items()]
            )
        )

class Community:

    community_id = None
    name = None
    description = None
    pic_url = None
    pic_url_large = None
    user = None
    thread = None
    created_at = None
    is_member = None
    is_admin = None
    members_count = None
    category = None
    url = None
    language = None

    def __init__(self, community_data):
        self.__dict__.update(community_data)
        self.user = User(self.user)

    def __str__(self):
        return 'Community({})'.format(
            ', '.join(
                [f'{key}={value}' for key, value in self.__dict__.items()]
            )
        )

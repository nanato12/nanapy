class LoginError(Exception):
    """
        login failed error
    """

class SignupError(Exception):
    """
        create account error
    """

class NotFoundUser(Exception):
    """
        not found user
    """

class NotFoundPost(Exception):
    """
        not found post
    """

class FollowError(Exception):
    """
        follow account error
    """

class PlayError(Exception):
    """
        post play error
    """

class ApplauseError(Exception):
    """
        post applause error
    """

class CommentError(Exception):
    """
        post comment error
    """

class LogoutError(Exception):
    """
        logout error
    """

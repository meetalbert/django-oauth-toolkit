from .compat import get_user_model
from .oauth2_backends import get_oauthlib_core

UserModel = get_user_model()
OAuthLibCore = get_oauthlib_core()


class OAuth2Backend(object):
    """
    Authenticate against an OAuth2 access token
    """

    def authenticate(self, request=None, **credentials):
        # Django skips any backend whose authenticate does not take request as its first argument.
        if request is not None:
            oauthlib_core = get_oauthlib_core()
            valid, r = oauthlib_core.verify_request(request, scopes=[])
            if valid:
                return r.user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

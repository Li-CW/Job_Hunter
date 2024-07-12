from utils.user.authentication import MyAuthentication


class BaseView:
    def get_authenticators(self):
        return MyAuthentication.get_authenticators(self.request)

    def get_permissions(self):
        return MyAuthentication.get_permissions(self.request)
from models import User, Connection

class AuthenticationBackend(object):

    def authenticate(self, credential, password):
        try:
            user = User.objects.get(username=credential)
        except User.DoesNotExist:
            try:
                email = User.objects.normalize_email(credential)
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class ConnectorBackend(object):

    def authenticate(self, connection_id):
        try:
            connection = Connection.objects.get(id=connection_id)
            return connection.user
        except Connection.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
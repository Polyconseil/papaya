from django.contrib.auth.models import User


class OpenIDBackend:
        """
        Authenticate against OpenID.
        """
        def authenticate(self, sreg_response):
            try:
                user = User.objects.get(username=sreg_response['nickname'])
                user.email = sreg_response['email']
            except User.DoesNotExist:
                count = User.objects.count()
                user = User.objects.create_user(
                    sreg_response['nickname'],
                    sreg_response['email'])
                # if this is the first user, make it an admin
                if not count:
                    user.is_staff = True
                    user.is_superuser = True
            user.first_name = sreg_response['fullname'].split(' ')[0]
            user.last_name = ' '.join(sreg_response['fullname'].split(' ')[1:])
            user.save()
            return user

        def get_user(self, user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None

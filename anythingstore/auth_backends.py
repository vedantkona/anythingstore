from typing import Optional
from  django.contrib.auth.backends import _AnyUser, ModelBackend

class FrontendLoginBackend(ModelBackend):
    def user_can_authenticate(self, user):
        if user.is_superuser:
            return False
        return super().user_can_authenticate(user)
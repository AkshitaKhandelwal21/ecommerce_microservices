from django.shortcuts import get_object_or_404

from auths.models import Users

class UserService:

    @staticmethod
    def register_user(data):
        return Users.objects.create_user(**data)

    @staticmethod
    def register_as_seller(user_id: int):
        user = get_object_or_404(Users, id=user_id)
        user.add_role("seller")
        return user

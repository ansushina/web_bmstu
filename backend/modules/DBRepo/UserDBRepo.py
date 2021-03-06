import jwt
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_jwt.serializers import jwt_payload_handler

from app.models.Profile import ProfileORM
from backend import settings
from modules.entities.Session import Session
from modules.entities.User import User
from django.contrib.auth.models import User as UserORM


class UserDBRepo:
    @staticmethod
    def decode_orm_user_profile(orm_user_profile):
        return User(id=orm_user_profile.id,
                    username=orm_user_profile.user.username,
                    email=orm_user_profile.user.email,
                    avatar=orm_user_profile.avatar,
                    created=orm_user_profile.created_at)

    @staticmethod
    def get(username) -> (User, str):
        try:
            orm_user = UserORM.objects.get(username=username)
            if not orm_user:
                return None, "NotExist"
            orm_user_profile = ProfileORM.objects.get(user_id=orm_user.id)
            if not orm_user_profile:
                return None, "NotExist"
            return UserDBRepo.decode_orm_user_profile(orm_user_profile), None
        except ObjectDoesNotExist:
            return None, "NotExist"

    @staticmethod
    def create(user: User) -> (User, str):
        orm_user = UserORM.objects.filter(email=user.email)
        if orm_user:
            return None, "invalid_email"
        orm_user = UserORM.objects.filter(username=user.username)
        if orm_user:
            return None, "invalid_username"
        orm_user = UserORM.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password
        )

        orm_user_profile = ProfileORM.objects.create(user=orm_user)
        orm_user.save()
        orm_user_profile.save()
        return UserDBRepo.decode_orm_user_profile(orm_user_profile), None

    @staticmethod
    def create_session(user: User) -> (Session, str):
        # orm_user = UserORM.objects.filter(
        #     username=user.username,
        #     password=user.password
        # )
        orm_user = auth.authenticate(
            username=user.username,
            password=user.password
        )
        if not orm_user:
            return None, "notExist"

        payload = jwt_payload_handler(orm_user)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        print(token)

        profile = ProfileORM.objects.get(user=orm_user.id)


        session = Session(
            username=orm_user.username,
            id=profile.id,
            token=token
        )

        return session, None

    @staticmethod
    def update(user: User) -> (User, str):
        user_fields, profile_fields = ['username', 'email'], ['avatar']
        fields_to_update = {'user': [], 'profile': []}
        profile = ProfileORM.objects.get(user=user.id)

        if not profile:
            return None, "NotExist"
        orm_user = UserORM.objects.get(pk=user.id)
        if not orm_user:
            return None, "NotExist"

        for key in user_fields:
            value = user.__getattribute__(key)
            if value != '':
                fields_to_update['user'].append(key)
                setattr(orm_user, key, value)

        value = user.__getattribute__('avatar')
        if value:
            fields_to_update['profile'].append('avatar')
            # print(value)
            setattr(profile, 'avatar', value)
        orm_user.save(update_fields=fields_to_update['user'])
        profile.save(update_fields=fields_to_update['profile'])
        return UserDBRepo.decode_orm_user_profile(profile), None

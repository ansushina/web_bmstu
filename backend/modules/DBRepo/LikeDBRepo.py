from typing import List

from app.models.Like import LikeORM
from app.models.Profile import ProfileORM
from modules.entities.Like import Like


class LikeDBRepo:
    @staticmethod
    def decode_orm_like(orm_like):
        return Like(id=orm_like.id,
                    value=orm_like.value,
                    author=orm_like.author.id,
                    film=orm_like.film.id)

    @staticmethod
    def get(like_id) -> Like:
        # print(like_id)
        orm_like = LikeORM.objects.get(pk=like_id)
        return LikeDBRepo.decode_orm_like(orm_like)

    @staticmethod
    def get_by_user_and_film(user_id, film_id) -> (Like, str):
        orm_like = LikeORM.objects.filter(author__user_id=user_id,
                                          film_id=film_id)[0]
        if orm_like:
            return LikeDBRepo.decode_orm_like(orm_like), None
        return None, 'NotExist'

    @staticmethod
    def update_by_user_and_film(user_id, film_id, like:Like) -> (Like, str):
        orm_like = LikeORM.objects.filter(author__user_id=user_id,
                                          film_id=film_id)
        if not orm_like:
            return None, 'NotExist'
        setattr(orm_like, 'value', like.value)
        orm_like.save()
        return LikeDBRepo.decode_orm_like(orm_like), None

    @staticmethod
    def update(like: Like) -> (Like, str):
        orm_like = LikeORM.objects.get(pk=like.id)
        if not orm_like:
            return None, 'NotExist'
        setattr(orm_like, 'value', like.value)
        orm_like.save()
        return LikeDBRepo.decode_orm_like(orm_like), None

    @staticmethod
    def create(user_id, film_id, like:Like) -> (Like, str):
        orm_like = LikeORM.objects.filter(author__user_id=user_id,
                                          film_id=film_id)
        if orm_like:
            return None, 'AlreadyExist'
        orm_author = ProfileORM.objects.get(user=user_id)
        orm_like = LikeORM.objects.create(
            film_id=film_id,
            author_id=orm_author.id,
            value=like.value
        )
        orm_like.save()
        return LikeDBRepo.decode_orm_like(orm_like), None

from typing import List

from app.models.Genre import GenreORM
from modules.entities.Genre import Genre


class GenreDBRepo:
    @staticmethod
    def decode_orm_genre(orm_genre):
        return Genre(id=orm_genre.id,
                     name=orm_genre.name)

    @staticmethod
    def get(genre_id) -> Genre:
        # print(genre_id)
        orm_genre = GenreORM.objects.get(pk=genre_id)
        return GenreDBRepo.decode_orm_genre(orm_genre)

    @staticmethod
    def get_all() -> List[Genre]:
        orm_genres = GenreORM.objects.all()
        genres = []
        for orm_genre in orm_genres:
            genres.append(GenreDBRepo.decode_orm_genre(orm_genre))
        return genres

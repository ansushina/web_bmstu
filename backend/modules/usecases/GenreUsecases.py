from typing import List

from modules.entities.Genre import Genre


class GenreUsecases:
    def __init__(self, genre_repo):
        self.genre_repo = genre_repo

    def get_genre(self, genre_id) -> Genre:
        genre = self.genre_repo.get(genre_id)
        return genre

    def get_all_genres(self) -> List[Genre]:
        genres = self.genre_repo.get_all()
        return genres


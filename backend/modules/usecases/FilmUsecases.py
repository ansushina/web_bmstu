from typing import List

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.entities.Film import Film


class FilmUsecases:
    def __init__(self, film_repo: FilmDBRepo):
        self.film_repo = film_repo

    def get_film(self, film_id) -> Film:
        #returns entity
        film = self.film_repo.get(film_id)
        return film

    def get_all_films(self, params: dict) -> List[Film]:
        films = self.film_repo.get_all(
            params
        )
        return films


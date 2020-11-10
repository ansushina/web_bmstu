from modules.DBRepo.FilmDBRepo import FilmDBRepo


class FilmUsecases:
    def __init__(self, film_repo: FilmDBRepo):
        self.film_repo = film_repo

    def get_film(self, film_id):
        #returns entity
        film = self.film_repo.get(film_id)
        return film

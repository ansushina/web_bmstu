from modules.entities.Like import Like


class LikeUsecases:
    def __init__(self, like_repo, film_repo):
        self.like_repo = like_repo
        self.film_repo = film_repo

    def get_like(self, like_id) -> Like:
        like = self.like_repo.get(like_id)
        return like

    def get_like_by_user_and_film(self, user_id, film_id) -> (Like, str):
        new_like, error = self.like_repo.get_by_user_and_film(user_id=user_id,
                                                              film_id=film_id)
        return new_like, error

    def update_like(self, film_id, like_id, value) -> (Like, str):
        like = Like(id=like_id, value=value)
        new_like, error = self.like_repo.update(like=like)
        self.film_repo.count_rating(film_id)
        return new_like, error

    def create_like(self, user_id, film_id, value) -> (Like, str):
        like = Like(value=value)
        new_like, error = self.like_repo.create(user_id=user_id,
                                                film_id=film_id,
                                                like=like)
        self.film_repo.count_rating(film_id)
        return new_like, error

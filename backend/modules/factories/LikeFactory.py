from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.LikeDBRepo import LikeDBRepo
from modules.usecases.LikeUsecases import LikeUsecases


class LikeFactory:
    @staticmethod
    def get_like_usecase() -> LikeUsecases:
        return LikeUsecases(LikeDBRepo(), FilmDBRepo())

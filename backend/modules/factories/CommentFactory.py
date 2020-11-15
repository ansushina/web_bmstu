from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.usecases.CommentUsecases import CommentUsecases


class CommentFactory:
    @staticmethod
    def get_comment_usecase() -> CommentUsecases:
        return CommentUsecases(CommentDBRepo())
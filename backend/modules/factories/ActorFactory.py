from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.usecases.ActorUsecases import ActorUsecases


class ActorFactory:
    @staticmethod
    def get_actor_usecase() -> ActorUsecases:
        return ActorUsecases(ActorDBRepo())

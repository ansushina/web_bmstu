from typing import List

from modules.entities.Actor import Actor
from tests.domain.ActorBuilder import ActorMother


class ActorDBRepoMock:

    @staticmethod
    def get(actor_id) -> Actor:
        return ActorMother.one().build()

    @staticmethod
    def get_all() -> List[Actor]:
        return [ActorMother.one().build(), ActorMother.two().build()]

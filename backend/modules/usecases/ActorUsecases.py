from typing import List

from modules.entities.Actor import Actor


class ActorUsecases:
    def __init__(self, actor_repo):
        self.actor_repo = actor_repo

    def get_actor(self, actor_id) -> Actor:
        actor = self.actor_repo.get(actor_id)
        return actor

    def get_all_actors(self) -> List[Actor]:
        actors = self.actor_repo.get_all()
        return actors


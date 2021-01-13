from typing import List

from django.core.exceptions import ObjectDoesNotExist

from app.models.Actor import ActorORM
from modules.entities.Actor import Actor


class ActorDBRepo:
    @staticmethod
    def decode_orm_actor(orm_actor):
        return Actor(id=orm_actor.id,
                     first_name=orm_actor.firstName,
                     last_name=orm_actor.lastName)

    @staticmethod
    def get(actor_id) -> Actor:
        # print(actor_id)
        try:
            orm_actor = ActorORM.objects.get(pk=actor_id)

            return ActorDBRepo.decode_orm_actor(orm_actor)

        except ObjectDoesNotExist:
            return None


    @staticmethod
    def get_all() -> List[Actor]:
        orm_actors = ActorORM.objects.all()
        actors = []
        for orm_actor in orm_actors:
            actors.append(ActorDBRepo.decode_orm_actor(orm_actor))
        return actors

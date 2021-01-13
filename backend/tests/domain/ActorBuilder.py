from modules.entities.Actor import Actor


class ActorMother:
    @staticmethod
    def one():
        actor = ActorBuilder()
        actor.first_name = 'actor1'
        actor.last_name = 'actor1'
        return actor

    @staticmethod
    def two():
        actor = ActorBuilder()
        actor.first_name = 'actor2'
        actor.last_name = 'actor1'
        return actor


class ActorBuilder:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.id = 0

    def build(self):
        return Actor(first_name=self.first_name,
                     last_name=self.last_name,
                     id=self.id)
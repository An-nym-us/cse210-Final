from game.actor import Actor
from game.point import Point
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []
        self.point = Point(0,0)

    def execute(self, cast):

        for group in cast.values():
            for actor in group:
                self.POINT = actor.get_position()
                print(self.point)
                pass







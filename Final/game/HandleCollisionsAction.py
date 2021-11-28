from game.actor import Actor
from game.point import Point
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []

    def execute(self, cast):
        pass





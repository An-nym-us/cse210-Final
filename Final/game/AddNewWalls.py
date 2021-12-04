from raylibpy import PINK
from game.action import Action
from game.point import Point
from game.Coins import Coin
from game.wall import Wall
import random
from game.input_service import InputService
from game import constants


class AddNewWalls(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []
        self.imawallArray = [Wall()]
        #self.add_new_wall_to_array






    def execute(self, cast):
        for group in cast.values():
            



            if(random.randrange(0, 100) == 7):
                cast["walls"].append(Wall())
                




        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        pass
        #raise NotImplementedError("execute not implemented in superclass")
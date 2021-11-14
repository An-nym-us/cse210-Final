
from game.action import Action
from game.point import Point
from game import constants

class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()
        


       #Called Every TICK
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        
        raise NotImplementedError("execute not implemented in superclass")





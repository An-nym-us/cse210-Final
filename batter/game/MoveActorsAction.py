
from game.action import Action
from game.point import Point
from game import constants

class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []
        
        


       #Called Every TICK
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """


        for group in cast.values():
            for actor in group:
                print("hello")
                
        #raise NotImplementedError("execute not implemented in superclass")





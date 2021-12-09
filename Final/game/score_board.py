
import random
from game.actor import Actor
from game.point import Point


class ScoreBoard(Actor):
    """Points earned. The responsibility of the ScoreBoard is to keep track of the player's points.
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self.points = 0
        self.is_scoreboard = True
        self.set_position(Point(1, 1))
        self.my_text = "777"
        self.set_text(f"Score: {self.points}")
        
   
        
    def get_text(self):
        self.points = self.points + 1 * 777
        self.my_text = f"Score: {self.points}"
        return self.my_text





    def execute(self, cast):
        for group in cast.values():
            pass





                




        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        pass
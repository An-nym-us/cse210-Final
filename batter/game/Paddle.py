from game.actor import Actor
from game.point import Point
from game import constants
from game.input_service import InputService



class Paddle(Actor):
    def __init__(self):
        super().__init__()
        IMAGE_PADDLE = constants.IMAGE_PADDLE
        self._image = IMAGE_PADDLE
        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT
        self.is_Paddle = True
        self.set_position(Point(300,550))
        self._velocity = Point(0, 0)
        self.direction = 0

    #def get_direction(self):








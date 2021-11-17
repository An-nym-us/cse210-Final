from game.actor import Actor
from game.point import Point
from game import constants



class Paddle(Actor):
    def __init__(self):
        super().__init__()
        IMAGE_PADDLE = constants.IMAGE_PADDLE
        self._image = IMAGE_PADDLE
        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT
        self.is_ball = False

        





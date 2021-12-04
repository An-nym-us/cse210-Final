from game.actor import Actor
from game.point import Point
from game import constants
from game.input_service import InputService



class Jetpack(Actor):
    def __init__(self):
        super().__init__()
        IMAGE_JETPACK = constants.IMAGE_JETPACK
        self._image = IMAGE_JETPACK
        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT
        self.is_jetpack = True
        self.can_i_move_up = True
        self.can_i_move_sown = True
        self.set_position(Point(300,400))
        self._velocity = Point(0, 0)
        self.direction = 0









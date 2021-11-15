from game.actor import Actor
from game.point import Point
from game import constants

class Ball():
    def __init__(self):
        super().__init__()
        
        BALL_IMAGE = constants.IMAGE_BALL
        self._image = BALL_IMAGE
        self._width = constants.BALL_WIDTH
        self._height = constants.BALL_HEIGHT
        self.position = Point(250,250)
        position = self.position
        self._velocity = Point(0, 0)



        #constructior Functions
        self.set_image(BALL_IMAGE)
        self.set_position(self.position)



    def set_image(self, BALL_IMAGE):
        self._image = BALL_IMAGE

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self.position

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def has_image(self):
        return self._image != ""

    def get_image(self):
        return self._image

    def get_velocity(self):

        return self._velocity









from game.actor import Actor
from game.point import Point
from game import constants

class Coin(Actor):
    def __init__(self):
        super().__init__()
        
        IMAGE_COIN = constants.IMAGE_COIN
        self._image = IMAGE_COIN
        self._width = constants.BALL_WIDTH
        self._height = constants.BALL_HEIGHT
        self.is_coin = True
        

        self._velocity = Point(10, 20)
        self.set_position(Point(200,200))
        



        #constructior Functions
        self.set_image(IMAGE_COIN)
        #self.set_position(self._position)



    def set_image(self, IMAGE_COIN):
        self._image = IMAGE_COIN

    #def set_position(self, position):
        #self._position = position

    def get_position(self):
        return self._position

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










from game.actor import Actor
from game.point import Point
from game import constants



class Brick(Actor):
    def __init__(self):
        super().__init__()

        #Set All Constants
        BRICK_IMAGE = constants.IMAGE_BRICK
        BRICK_WIDTH = constants.BRICK_WIDTH
        BRICK_HEIGHT = constants.BRICK_HEIGHT
        self.position = Point(0 , 0)
        position = self.position



        #Constructor Functions
        self.set_position(self.position)
        self.set_image(BRICK_IMAGE)




    def set_image(self, brick_image):
        self._image = brick_image


    #Sets the position of the brick on the screen
    def set_position(self, position):
        self._position = position









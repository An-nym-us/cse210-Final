
import random
from game.actor import Actor
from game.point import Point
from game import constants



class Wall(Actor):
    def __init__(self):
        super().__init__()

        #Set All Constants
        WALL_IMAGE = constants.IMAGE_WALL
        BRICK_WIDTH = constants.BRICK_WIDTH
        BRICK_HEIGHT = constants.BRICK_HEIGHT
        self.is_wall = True
        self._velocity = Point(-10, 0)
        #print("Wall created")
        #Sets the postion to 0, 0 at spawn if the set postion is not defind
        if self.set_position(Point(700,random.randrange(20, 500))) is None:
            self.set_position(Point(700,random.randrange(20, 500)))
       

        



        #Constructor Functions
        self.set_image(WALL_IMAGE)




    def set_image(self, wall_image):
        self._image = wall_image


    #Sets the position of the brick on the screen
    def get_position(self):
        return self._position









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
        #self.position = Point(0 , 0)
        self.set_position(Point(0,0))
        position = self.position
        self._y = 0
        self._x = 0
        



        #Constructor Functions
        self.set_position(self.position)
        self.set_image(BRICK_IMAGE)




    def set_image(self, brick_image):
        self._image = brick_image


    #Sets the position of the brick on the screen
    def set_position(self, position):
        self._position = position


    def get_position(self):
        self.position



    def get_x(self):
        """Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x


    def get_y(self):
        """Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y



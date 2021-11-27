
from game.action import Action
from game.point import Point
from game.Coins import Coin
from game.input_service import InputService
from game import constants


class MoveActorsAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []
        self.input_service = InputService()
        self.yloc= 0
        
        


       #Called Every TICK
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """


        for group in cast.values():
            for actor in group:
                
                velocity_x = actor.get_velocity().get_x()
                velocity_y = actor.get_velocity().get_y()

                new_point_x = actor.get_position().get_x()
                new_point_y = actor.get_position().get_y()

                

                
                #ensures that it is only moving the position of the ball and no other obejct
                try:
                    if actor.is_coin == True:
                        #This Moves The Ball Accross The Screen
                        new_point_x = velocity_x + new_point_x
                        new_point_y = velocity_y + new_point_y
                        actor.set_position(Point(new_point_x, new_point_y))
                except:
                    pass

                
                try:
                    if actor.is_jetpack is not None:
                        direction = self.input_service.get_direction()
                        x_locaction = actor.get_position().get_x()
                        y_direction = direction.get_y()                       
                        y_direction = y_direction * 15                        
                        self.yloc = y_direction + self.yloc
                        actor.set_position(Point( x_locaction,self.yloc))
                except:
                    pass


                


                
                
        #raise NotImplementedError("execute not implemented in superclass")





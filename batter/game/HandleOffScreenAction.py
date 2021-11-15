from game.action import Action
from game.point import Point
from game.Ball import Ball
import random
from game import constants



class HandleOffScreenAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []


    def execute(self, cast):

        for group in cast.values():
            for actor in group:
                


                

                
                
                if actor.is_ball == True:
                    #Make the ball change direction if it hits the left or right wall
                    velocity_x = actor.get_velocity().get_x()
                    velocity_y = actor.get_velocity().get_y()

                    new_point_x = actor.get_position().get_x()
                    new_point_y = actor.get_position().get_y()
                    if new_point_y > 600 or new_point_y < 0:
                        velocity_y = velocity_y * -1
                        actor.set_velocity(Point(velocity_x, velocity_y))

                    #Make the ball change direction if it hits the top or bottom wall
                    if new_point_x > 800 or new_point_x < 0:
                        velocity_x = velocity_x * -1
                        actor.set_velocity(Point(velocity_x, velocity_y))
                    



        pass






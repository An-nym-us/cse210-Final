from game.actor import Actor
from game.point import Point

from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    def __init__(self):
        super().__init__()
        self.tag_list = []
        self.point = Point(0,0)

        self.is_collisions = False

        #wall location values.
        self.wall_y_value = 0
        self.wall_x_value = 0

        #jetpack loction values.
        self.jetpack_y_value = 0
        self.jetpack_y_value_upper_range = 0
        self.jetpack_y_value_lower_range = 0

        self.jetpack_x_value = 0

    def end_the_game(self):
        
        return self.end_game

    def execute(self, cast):

        for group in cast.values():
            for actor in group:
                try:
                   if actor.is_wall is not None:

                        #Get the wall actors x position when it lines up with the jetpack
                        self.wall_y_value = actor.get_position().get_y()
                        self.wall_x_value = actor.get_position().get_x()

                        #check if wall is in range of the paddle x-value
                        if self.wall_x_value >= 280 and self.wall_x_value <=320:


                            for group_jet in cast.values():
                                for get_jetpack in group_jet:
                                    try:
                                        if get_jetpack.is_jetpack is not None:
                                            
                                            #get jetpack current loctions
                                            self.jetpack_y_value = get_jetpack.get_position().get_y()
                                            self.jetpack_y_value_upper_range = self.jetpack_y_value + 50
                                            self.jetpack_y_value_lower_range = self.jetpack_y_value - 50
                                            self.jetpack_x_value = get_jetpack.get_position().get_x()

                                            #final check to end game!!!
                                            if self.wall_y_value >= self.jetpack_y_value_lower_range and self.wall_y_value <= self.jetpack_y_value_upper_range:
                                                self.end_game = True
                                    except:
                                        pass
                except:
                    pass
                pass







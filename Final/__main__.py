import random
#from Final.game import score_board
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.wall import Wall
from game.Coins import Coin
from game.Jetpack import Jetpack
from game.AddNewWalls import AddNewWalls
from game.score_board import ScoreBoard
# from game.control_actors_action import ControlActorsAction
from game.HandleCollisionsAction import HandleCollisionsAction
from game.HandleOffScreenAction import HandleOffScreenAction
from game.MoveActorsAction import MoveActorsAction




def main():

    # create the cast {key: tag, value: list}
    cast = {}
    x = 0
    y = 0
    k = 0


    wall_array = []


    cast["walls"] = [Wall()]


    # TODO: Create bricks here and add them to the list

    cast["coins"] = []
    # TODO: Create a ball here and add it to the list

    cast["jetpack"] = [Jetpack()]
    cast["scoreboard"] = [ScoreBoard()]
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_actions = HandleOffScreenAction()
    handle_collisions_action = HandleCollisionsAction()
    Add_New_Walls = AddNewWalls()
    score_board = ScoreBoard()

    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = [move_actors_action, handle_off_screen_actions, handle_collisions_action, Add_New_Walls, score_board]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("jetpackjoyride");
    #audio_service.start_audio()
   # audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()

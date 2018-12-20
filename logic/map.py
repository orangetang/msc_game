"""
TODO:
    *header docstring
    *method implementation
"""

import logging
from logic.cow import Cow

__version__ = "0.1.0"
__author__ = "orangetang"

_log = logging.getLogger(__name__)

# Proportion - percentage of map expected to contain the corresponding tile
# spread chance - initial likelihood of the initial tile spawning a neighbor in any given cardinal direction
TERRAIN_PROPORTION
MIN_WATER_PROPORTION
WATER_SPREAD_CHANCE
MAX_WATER_PROPORTION
MIN_FOOD_PROPORTION
FOOD_SPREAD_CHANCE
MAX_FOOD_PROPORTION
# The spread chance must decrease by at least this much for the number of tiles the current node is from the initial
# node (terrain, water, food)
MINIMUM SPREAD DECAY
# Likelihood of a natural disaster occurring at the beginning of a turn
DISASTER_CHANCE


# TODO docs
class Map(object):
    """"""

    # TODO docs
    def __init__(self, x_dimension=250, y_dimension=250, herd_size=10):
        """

        :param x_dimension:
        :param y_dimension:
        :param herd_size:
        """
        # max dimensions of the map
        self._x_dimension = x_dimension
        self._y_dimension = y_dimension
        # sparse 2 dimensional array representing the current arrangement of the map
        self.map_dict = {}
        self.cows = {}
        self.water_features = {}
        self.food_stockpiles = {}

        self.generate_terrain()
        self.generate_water()
        self.generate_food()
        self.spawn_herd(herd_size)

    # TODO include 'hazards'
    def generate_terrain(self):
        """Creates randomly placed impassible locations on the map"""

    def generate_water(self):
        """Creates randomly placed water locations on the map"""

    def generate_food(self):
        """Creates randomly placed food locations on the map"""

    # TODO docs
    def spawn_herd(self, herd_size):
        """
        Spawns cows in a loosely grouped herd
        :param herd_size:
        :return:
        """

    def birth_calf(self, x_coordinate, y_coordinate):
        """
        Spawns a 'baby' cow
        :param x_coordinate:
        :param y_coordinate:
        :return:
        """

    def natural_disaster(self):
        """Causes a natural disaster"""

    # Movement for cows
    # Rules:
    # 1. Cows may not enter terrain
    # 2. Cows may enter edge water or food spaces, however:
    #   a. Cows may not end the turn on water or food spaces
    #   b. Cows have a chance to contaminate water and food "blobs"
    #   c. Cows may not enter interior water and food spots

    def move_north(self, bovine_identifier):
        """
        Move cow one tile up
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_south(self, bovine_identifier):
        """
        Move cow one tile down
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_east(self, bovine_identifier):
        """
        Move cow one tile right
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_west(self, bovine_identifier):
        """
        Move cow one tile left
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_northeast(self, bovine_identifier):
        """
        Move cow one tile down, one tile left
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_northwest(self, bovine_identifier):
        """
        Move cow one tile up, one tile left
        :param bovine_identifier: id of the cow to moove
        :return: whether or not the cow was able to move to the new position
        """

    def move_southeast(self, bovine_identifier):
        """
        Move cow one tile down, one tile right
        :param bovine_identifier: id of the cow to moove
        :return: Whether or not the cow was able to move to the new position
        """

    def move_southwest(self, bovine_identifier):
        """
        Move cow one tile down, one tile left
        :param bovine_identifier: id of the cow to moove
        :return: hether or not the cow was able to move to the new position
        """

    def grow_herd(self):
        """'Grow' all of the cows on the map, spawns baby cows, removes decayed cow 'remains'"""

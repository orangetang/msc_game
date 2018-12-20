"""
TODO:
    *header docstring
    *finish stubbing out game base class logic
    *stub out getting and saving game states, create save data schema
    *method implementation
    *add pytests
    *create a concrete instance of the game in a new python file
"""

import logging
from abc import abstractmethod
from logic.map import Map

__version__ = "0.1.0"
__author__ = "orangetang"

_log = logging.getLogger(__name__)


# TODO docs
class BaseGame(object):
    """"""

    # TODO docs
    def __init__(self, days_per_turn=20):
        """

        :param days_per_turn:
        """

        self.turn = 0
        self.day = 0
        self._days_per_turn = days_per_turn

        self.map = Map()

    @abstractmethod
    def next_day(self):
        """
        Logic which occurs during each day of a turn
        """

    def next_turn(self):
        """
        Logic which occurs at the start of each turn
        """

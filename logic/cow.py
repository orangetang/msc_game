"""
TODO:
    *header docstring
    *method implementation
"""

import logging

__version__ = "0.1.0"
__author__ = "orangetang"

_log = logging.getLogger(__name__)

# Rules for the life and death of cows
DISEASE_MORTALITY_RATE
MAXIMUM_AGE
MAXIMUM_HUNGER
MAXIMUM_THIRST


class Cow(object):
    """Object for managing the state of bovine entities"""

    # TODO docs
    def __init__(self, x_position, y_position, initial_age=0, initial_disease_duration=None):
        """

        :param x_position:
        :param y_position:
        :param initial_age:
        :param initial_disease_duration:
        """

        self.bovine_identifier = id(self)
        # biological sex of the cow
        # TODO
        self.sex
        # Number of turns remaining in gestation period
        self.gestation_duration = None
        self.x_position = x_position
        self.y_position = y_position
        self.alive = True
        # Number of turns since the cow was "born"
        self.age = initial_age
        # Number of turns since the cow has quenched its thirst
        self.thirst_level = 0
        # Number of turns since the cow has eaten
        self._hunger_level = 0
        # Number of turns remaining for the duration of the disease
        self.disease_duration = initial_disease_duration

    def _check_thirst(self):
        """
        :return: Whether the cow has surpassed maximum thirst level
        """

    def _check_starvation(self):
        """
        :return: Whether the cow has surpassed maximum hunger level
        """

    def _manage_disease(self):
        """Updates the duration and disease status of the cow"""

    def _check_old_age(self):
        """
        :return: Whether the cow has died
        """

    def gives_birth(self):
        """
        :return: Whether the cow gives birth on the given turn
        """

    def is_alive(self):
        """
        Compares the various values and manages health at the beginning of each turn
        :return: Whether the cow has met an untimely end
        """

    def kill(self):
        """
        The cow has passed away
        """

    def is_decayed(self):
        """
        :return: Whether the cow's body has decayed
        """

    def grow(self):
        """
        Determines if the cow is alive, updates hunger, thirst, gestation duration and disease duration
        """

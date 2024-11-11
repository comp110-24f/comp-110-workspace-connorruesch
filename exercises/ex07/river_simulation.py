"""A module for conducting a river simulation."""

from exercises.ex07.river import River

__author__: str = "730736398"

# Create our river instance.
my_river: River = River(10, 2)

# Conduct one week in the River's life.
my_river.one_river_week()

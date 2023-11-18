# __init__.py for soccer_league package

# Importing key classes from the package for easier access
from .stat_tracker import StatTracker
from .team import Team
from .game import Game

# Define what gets imported with "from soccer_league import *"
__all__ = ['StatTracker', 'Team', 'Game', 'Team', 'GameTeam']

# You can also include any initialization code needed for your package here

import pandas as pd
import pdb
from futbol_league.game import Game
from futbol_league.team import Team
from futbol_league.game_team import GameTeam

class CSVDataReader:
    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)

class StatTracker:
    def __init__(self, file_path):
        self.games = self.create_objects_from_csv(Game, file_path['games'])
        self.teams = self.create_objects_from_csv(Team, file_path['teams'])
        self.game_teams = self.create_objects_from_csv(GameTeam, file_path['game_teams'])
        pdb.set_trace()

    def create_objects_from_csv(self, cls, file_path):
        data = CSVDataReader.read_csv(file_path)
        return [cls(row) for _, row in data.iterrows()]


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
        self.games = self.games_array(file_path['games'])
        self.teams = self.teams_array(file_path['teams'])
        self.game_teams = self.game_teams_array(file_path['game_teams'])

    def games_array(self, games_path):
        games_list = []
        games_data = CSVDataReader.read_csv(games_path)
        for index, game_row in games_data.iterrows():
            game = Game(game_row)
            games_list.append(game)
        return games_list
    
    def teams_array(self, teams_path):
        teams_list = []
        teams_data = CSVDataReader.read_csv(teams_path)
        for index, team_row in teams_data.iterrows():
            team = Team(team_row)
            teams_list.append(team)
        return teams_list
    
    def game_teams_array(self, game_teams_path):
        game_teams_list = []
        game_teams_data = CSVDataReader.read_csv(game_teams_path)
        for index, game_team_row in game_teams_data.iterrows():
            game_team = GameTeam(game_team_row)
            game_teams_list.append(game_team)
        return game_teams_list


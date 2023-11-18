import pdb

class Team:
    def __init__(self, team_data):
        self.team_id = team_data['team_id']
        self.franchiseId = team_data['franchiseId']
        self.team_name = team_data['teamName']
        self.abbreviation = team_data['abbreviation']
        self.stadium = team_data['Stadium']
        self.link = team_data['link']


class Game:
    def __init__(self, game_data):
        self.game_id = game_data['game_id']
        self.season = game_data['season']
        self.type = game_data['type']
        self.date_time = game_data['date_time']
        self.away_team_id = game_data['away_team_id']
        self.home_team_id = game_data['home_team_id']
        self.away_goals = game_data['away_goals']
        self.home_goals = game_data['home_goals']
        self.venue = game_data['venue']
        self.venue_link = game_data['venue_link']


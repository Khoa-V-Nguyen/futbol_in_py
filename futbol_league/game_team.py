class GameTeam:
    def __init__(self, game_team_data):
        self.game_id = game_team_data['game_id']
        self.team_id = game_team_data['team_id']
        self.hoa = game_team_data['HoA']
        self.result = game_team_data['result']
        self.settled_in = game_team_data['settled_in']
        self.head_coach = game_team_data['head_coach']
        self.goals = game_team_data['goals']
        self.shots = game_team_data['shots']
        self.tackles = game_team_data['tackles']
        self.pim = game_team_data['pim']
        self.power_play_opportunities = game_team_data['powerPlayOpportunities']
        self.face_off_win_percentage = game_team_data['faceOffWinPercentage']
        self.give_aways = game_team_data['giveaways']
        self.take_aways = game_team_data['takeaways']


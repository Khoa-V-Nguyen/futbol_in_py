import pytest
from futbol_league.stat_tracker import StatTracker 

# Fixture for setting up StatTracker
@pytest.fixture(scope="module")
def stat_tracker():
    game_path = './data/games.csv'
    team_path = './data/teams.csv'
    game_teams_path = './data/game_teams.csv'

    locations = {
        'games': game_path,
        'teams': team_path,
        'game_teams': game_teams_path
    }

    return StatTracker(locations)

def test_stat_tracker_exists(stat_tracker):
    assert isinstance(stat_tracker, StatTracker)

def test_highest_total_score(stat_tracker):
    assert stat_tracker.highest_total_score() == 11

def test_lowest_total_score(stat_tracker):
    assert stat_tracker.lowest_total_score() == 0


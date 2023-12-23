from flask import render_template, request, redirect, url_for
from app import app
from nba_api.stats.endpoints import playercareerstats
import random
def get_player_stats(player_id):
    # Use NBA API to get player career stats
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    stats = career.get_data_frames()[0]
    return stats
# Function to generate random player data
def generate_random_player():
    first_names = ['LeBron', 'Kevin', 'Stephen', 'Kawhi', 'Giannis', 'Anthony', 'James', 'Chris', 'Joel', 'Luka',
                   'Russell', 'Damian', 'Paul', 'Jimmy', 'Klay', 'Jayson', 'Devin', 'Donovan', 'Zion', 'Trae']
    last_names = ['James', 'Durant', 'Curry', 'Leonard', 'Antetokounmpo', 'Davis', 'Harden', 'Paul', 'Embiid', 'Doncic',
                  'Westbrook', 'Lillard', 'George', 'Butler', 'Thompson', 'Tatum', 'Booker', 'Mitchell', 'Williamson', 'Young']
    nba_teams = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls',
                 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors',
                 'Houston Rockets', 'Indiana Pacers', 'LA Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies',
                 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks',
                 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers',
                 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
    return {
        'name': f'{random.choice(first_names)} {random.choice(last_names)}',
        'team': random.choice(nba_teams),
        'points': round(random.uniform(10, 30), 1),
        'assists': round(random.uniform(2, 10), 1),
        'rebounds': round(random.uniform(5, 15), 1),
  # Replace with actual image URL logic
    }
# Generate dummy data for 50 players
dummy_players = [generate_random_player() for _ in range(50)]
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')
@app.route('/player_stats')
def player_stats():
    return render_template('player_stats.html', players=dummy_players)
# Redirect route for back button
@app.route('/back_to_main')
def back_to_main():
    return redirect(url_for('index'))
# Route to get NBA player stats using NBA API
@app.route('/api/player_stats/<int:player_id>', methods=['GET'])
def api_player_stats(player_id):
    stats = get_player_stats(player_id)
    return stats.to_json(orient='records')































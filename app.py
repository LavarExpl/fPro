from flask import Flask, render_template
app = Flask(__name__)
# Sample data for demonstration
random_players = [
   {'name': 'Player 1', 'team': 'Team A', 'points': 20, 'assists': 5, 'rebounds': 10},
   {'name': 'Player 2', 'team': 'Team B', 'points': 15, 'assists': 7, 'rebounds': 8},
   # Add more player data as needed
]
@app.route('/')
def index():
   return render_template('your-html-file.html', random_players=random_players)
if __name__ == '__main__':
   app.run(debug=True)















from flask import Flask, jsonify, request, render_template
import ipl
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response =ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)

@app.route('/api/teamrecord')
def teamrecord():
    team = request.args.get('team')
    response =ipl.teamRecord(team)
    print(response)
    return jsonify(response)

@app.route('/api/batsmanrecord')
def batsmanrecord():
     batter = request.args.get('batter')
     response = ipl.batsmanrecord(batter)
     return jsonify(response)

@app.route('/api/seasonwinner')
def seasonwinner():
     SeasonWinner= ipl.seasonwinner()
     return jsonify(SeasonWinner)

@app.route('/api/venues')
def venue():
     venues = ipl.venues()
     return jsonify(venues)

@app.route('/api/teamatvenue')
def teamvenue():
     team = request.args.get('team')
     venue = request.args.get('venue')
     teamatvenue = ipl.teamatvenue(team,venue)
     return jsonify(teamatvenue)

@app.route('/api/batsmanruns')
def batsmanruns():
    batsman = ipl.allbatsmanstats()
    return jsonify(batsman)

@app.route('/api/noofsix')
def noofsix():
    noofsix = ipl.noofsix()
    return jsonify(noofsix)

@app.route('/api/powerhitters')
def powerhittersoflast5overs():
    powerhitter = ipl.powerhitters()
    return jsonify(powerhitter)

@app.route('/api/batsman-runs-against-all-teams')
def batsmanvsall():
    batsman = request.args.get('batsman')
    batsman= ipl.batsmanvsall(batsman)
    return jsonify(batsman)

app.run(debug=True)
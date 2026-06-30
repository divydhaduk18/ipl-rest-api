from flask import Flask,jsonify,request
import ipl as ipl 

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    
    response = ipl.teamVteamAPI(team1,team2)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = ipl.teamRecordAPI(team_name)
    
    return jsonify(response)

@app.route('/api/matches')
def matches():
    
    team = request.args.get('team')
    response = ipl.matchesAPI(team)
    
    return jsonify(response)

@app.route('/api/match')
def match():
    id = int(request.args.get('id'))
    response = ipl.matchDetailsAPI(id)
    
    return jsonify(response)

@app.route('/api/seasons')
def seasons():
    
    response = ipl.seasonAPI()
    
    return jsonify(response)

@app.route('/api/points-table')
def pointsTable():
    s = request.args.get('season')
    
    points_table = ipl.pointsTable(s)
    
    return jsonify(points_table)

app.run(debug=True)
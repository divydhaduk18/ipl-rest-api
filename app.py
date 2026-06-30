from flask import Flask,jsonify,request
import ipl as ipl 

app = Flask(__name__)
app.json.sort_keys = False

from flask import jsonify

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to IPL REST API",
        "version": "1.0",
        "available_endpoints": {
            "Get all teams": "/api/teams",
            "Head to Head": "/api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings",
            "Team Record": "/api/team-record?team=Mumbai Indians",
            "All Matches of a Team": "/api/matches?team=Mumbai Indians",
            "Match Details": "/api/match?id=1312200",
            "Points Table": "/api/points-table?season=2022"
        }
    })

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

if __name__ == "__main__":
    app.run(debug=True)
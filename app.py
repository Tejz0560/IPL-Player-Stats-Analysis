from flask import Flask,request,jsonify
import ipl
import ipl_record

app = Flask(__name__)

@app.route("/")
def home():
    response = {
        "A-message" : "Welcome to the IPL api service by Tejas Bidwai. Here are the apis to help you : ",
        "api/allteams":" List of all Teams",
        "api/teamvteam":"It gives team1 vs team2 stats. Input required team1 = first team, team2 = second team. eg,: api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings"
    }
    return jsonify(response)

@app.route("/api/allteams")
def teams():
    response = ipl.teamsAPI()
    return jsonify(response)

@app.route("/api/teamvteam")
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1,team2)

    return jsonify(response)

@app.route("/api/teamrecord")
def teamrecord():
    team = request.args.get("team")

    response = ipl_record.teamAPI(team)

    return jsonify(response)


app.run(debug=True)
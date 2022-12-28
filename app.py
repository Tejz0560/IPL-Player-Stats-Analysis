from flask import Flask,request,jsonify
import ipl
import ipl_record

app = Flask(__name__)

@app.route("/")
def home():
    response = {
        "A-message" : "Welcome to the IPL api service by Tejas Bidwai. Here are the apis to help you : ",
        "api/allteams":" List of all Teams",
        "api/teamvteam":"It gives team1 vs team2 stats. Input required team1 = first team, team2 = second team. eg,: api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings",
        "api/teamrecord":"It gives team stats vs all other teams. Input required team = name of team. eg.: api/teamrecord?team=Mumbai Indians",
        "api/batsmanrecord":"It gives batsman stats vs all other teams. Input required batsman = name of batsman. eg.: api/batsmanrecord?batsman=V Kohli",
        "api/bowlerrecord":"It gives bowler stats vs all other teams. Input required bowler = name of bowler. eg.: api/bowlerrecord?bowler=JJ Bumrah"
        

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

@app.route("/api/batsmanrecord")
def batsmanrecord():
    batsman = request.args.get("batsman")

    response = ipl_record.batsmanAPI(batsman)

    return jsonify(response)

@app.route("/api/bowlerrecord")
def bowlerrecord():
    bowler = request.args.get('bowler')

    response = ipl_record.bowlerAPI(bowler)

    return jsonify(response)

app.run(debug=True)
from flask import Flask,request,jsonify
import ipl

app = Flask(__name__)

@app.route("/")
def home():
    response = {
        
        "api/allteams":" List of all Teams",
        "A-message" : "Welcome to the IPL api service by Tejas Bidwai. Here are the apis to help you : "
    }
    return jsonify(response)

@app.route("/api/allteams")
def teams():
    response = ipl.teamsAPI()
    return jsonify(response)


app.run(debug=True)
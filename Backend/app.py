from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
from Graph import Graph
from WaitList import WaitList
from helper import create_pair, random_donor, random_recipient

G = None
W = None

@app.route("/graph/init", methods=["GET"])
def graph_init():
    global G
    name = request.args.get('name')
    if name == '':
        return {}
    G = Graph(name)
    gData = {"Graph": G.G, "Pairs": G.P, "Size": G.size, "Name": G.name}
    return json.dumps(gData) 

@app.route("/graph/save", methods=["POST"])
def graph_save():
    if G != None:
        G.save()
    else:
        return 'No Graph to Save', 400
    return json.dumps({})

@app.route("/graph/deselect", methods=["POST"])
def graph_deselect():
    global G
    G = None
    return json.dumps({})

@app.route("/graph/add", methods=["POST"])
def graph_add():
    data = request.get_json()
    if data['Random'] == True:
        Pair = create_pair(random_donor(), random_recipient())
    else:
        Pair = create_pair(data['Donor'], data['Recipient'])
    return json.dumps(G.add_pair(Pair))

@app.route("/graph/clear", methods=["DELETE"])
def graph_clear():
    return json.dumps(G.clear())

@app.route("/graph/show", methods=["GET"])
def graph_show():
    return json.dumps(G.print_graph())

@app.route("/waitlist/init", methods=["GET"])
def waitlist_init():
    global W
    name = request.args.get('name')
    if name == '':
        return {}
    W = Waitlist(name)
    wData = {"Waitlist": W.W, "Name": W.name, "Size": W.size}
    return json.dumps(gData) 

@app.route("/waitlist/add", methods=["POST"])
def waitlist_add():
    data = request.get_json()
    if data['Random'] == True:
        Recipient = random_recipient()
    else:
        Recipient = data['Recipient']
    return json.dumps(W.add_recipient(Recipient))

@app.route("/waitlist/save", methods=["POST"])
def waitlist_save():
    if W != None:
        W.save()
    else:
        return 'No Graph to Save', 400
    return json.dumps({})

@app.route("/waitlist/show", methods=["GET"])
def waitlist_show():
    return json.dumps(W.print_list())

@app.route("/simulate", methods=["GET"])
def simulate():
    days = request.args.get('days')
    chance = request.args.get('chance')
    TG = Graph()
    dead = 0
    saved = 0
    count = 0
    for i in range(days):
        rand = random.randint(0, 99)
        if rand < chance:
            saved += TG.add_pair(create_pair(random_donor(), random_recipient()), "sim")
            count += 1
        dead += TG.pass_day(1, "sim")
    Data = {
        "Pairs": count,
        "Dead": dead,
        "Saved": saved,
        "Still on List": TG.size
    }
    return json.dumps(Data)
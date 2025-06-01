import requests
import json
import time
import threading
from . import server

def goals(id):
    tm = server.teams()

    team_of_id = set()
    for i in tm:
        for j in i['players']:
            if j == id:
                team_of_id.add(i['id'])

    mm = server.matches()
    #print (mm)

    ans = []
    for i in mm:
        if i["team1"] not in team_of_id and i["team2"] not in team_of_id:
            continue

        match = server.match(i['id'])

        for j in match:
            if j['player'] == id:
                ans.append([j['match'], j['minute']])

    return ans
import requests
import json
import time
import threading
from . import server

def stats(name):
    tm = server.teams()

    id_team = []
    for i in tm:
        id_team.append(i['id'])

    nm_tm = dict()
    for i in id_team:
        team = server.team(i)

        nm_tm[team['name']] = i

    name = name[1:-1]

    if (nm_tm.get(name) == None):
        return [0, 0, 0]

    mm = server.matches()

    wn = 0
    ls = 0
    gl = 0
    id = nm_tm[name]
    for i in mm:

        if i['team1'] == id:
            if i['team1_score'] > i['team2_score']:
                wn += 1
            elif i['team1_score'] < i['team2_score']:
                ls += 1
            gl += i['team1_score']
            gl -= i['team2_score']

        if i['team2'] == id:
            if i['team1_score'] < i['team2_score']:
                wn += 1
            elif i['team1_score'] > i['team2_score']:
                ls += 1
            
            gl -= i['team1_score']
            gl += i['team2_score']

    return [wn, ls, gl]

import requests
import json
import time
import threading
from . import server

def versus(id1, id2):
    tm = server.teams()

    pl_tm = dict()
    for i in tm:
        for j in i["players"]:
            if pl_tm.get(j) == None:
                pl_tm[j] = set()
            
            pl_tm[j].add(i['id'])

    if pl_tm.get(id1) == None or pl_tm.get(id2) == None:
        return 0
    
    mm = server.matches()

    mt = 0
    for i in mm:
        if i['team1'] in pl_tm[id1] and i['team2'] in pl_tm[id2]:
            mt += 1
        if i['team2'] in pl_tm[id1] and i['team1'] in pl_tm[id2]:
            mt += 1
    return mt
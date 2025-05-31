import requests
import json
import time

server = "https://lksh-enter.ru"

qs = server + "/teams"
data_teams = requests.get(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'})
tm = json.loads(data_teams.text)

id_team = []
for i in tm:
    id_team.append(i['id'])

nm_tm = dict()
for i in id_team:
    qs = server + '/teams/' + str(i)
    data_team = requests.get(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'})
    team = data_team.json()

    nm_tm[team['name']] = i


id_players = []
pl_tm = dict()
for i in tm:
    for j in i["players"]:
        id_players.append(j)
        
        if pl_tm.get(j) == None:
            pl_tm[j] = set()
        
        pl_tm[j].add(i['id'])
id_players.sort()

players = []
for i in range(len(id_players)):
    if (i != 0 and id_players[i - 1] == id_players[i]):
        continue

    qs = server + '/players/' + str(id_players[i])
    data_player = requests.get(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'})
    if data_player.status_code == 429:
        time.sleep(1)
        data_player = requests.get(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'})

    player = data_player.json()

    players.append(player['name'] + " " + player['surname'])
players.sort()

print(*players, sep = '\n')

qs = server + "/matches"
data_matches = requests.get(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'})
mm = json.loads(data_matches.text)

def kom(id):
    wn = 0
    ls = 0
    gl = 0
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

def ply(id1, id2):
    print(id1, id2)
    if pl_tm.get(id1) == None or pl_tm.get(id2) == None:
        return 0
    
    mt = 0
    for i in mm:
        print(i['id'])
        if i['team1'] in pl_tm[id1] and i['team2'] in pl_tm[id2]:
            mt += 1
        if i['team2'] in pl_tm[id1] and i['team1'] in pl_tm[id2]:
            mt += 1
    return mt

while(1):
    s = input()

    if s[0] == 's':
        a = s.split()
        name = ""
        for i in range(1, len(a)):
            if (i != 1):
                name += ' '

            name += a[i]
        
        if (nm_tm.get(name) == None):
            print("0 0 0")
        else:
            print(*kom(nm_tm[name[1:-1]]))
    else:
        a, id1, id2 = s.split()
        id1 = int(id1)
        id2 = int(id2)
        print(ply(id1, id2))

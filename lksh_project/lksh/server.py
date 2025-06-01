import requests
import json
import time

server = "https://lksh-enter.ru"
auth_str = 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'

def teams():
    qs = server + "/teams"
    data_teams = requests.get(qs, headers={'Authorization': auth_str})

    if data_teams.status_code == 429:
        time.sleep(1)
        data_teams = requests.get(qs, headers={'Authorization': auth_str})
    
    ans = []
    if data_teams.status_code == 200:
        ans = json.loads(data_teams.text)
    
    return ans

def matches():
    qs = server + "/matches"

    data_matches = requests.get(qs, headers={'Authorization': auth_str})
    if data_matches.status_code == 429:
        time.sleep(1)
        data_matches = requests.get(qs, headers={'Authorization': auth_str})
    
    ans = []
    if data_matches.status_code == 200:
        ans = json.loads(data_matches.text)
    
    return ans

def team(id):
    qs = server + '/teams/' + str(id)
    data_team = requests.get(qs, headers={'Authorization': auth_str})
    if data_team.status_code == 429:
        time.sleep(1)
        data_team = requests.get(qs, headers={'Authorization': auth_str})
    
    ans = []
    if data_team.status_code == 200:
        ans = json.loads(data_team.text)
    
    return ans


def match(id):
    qs = server + "/goals"
    
    data_match = requests.get(qs, params= [{"match_id", id}], headers={'Authorization': auth_str})
    if data_match.status_code == 429:
        time.sleep(1)
        data_match = requests.get(qs, params= [{"match_id", id}], headers={'Authorization': auth_str})
    
    ans = []
    if data_match.status_code == 200:
        ans = json.loads(data_match.text)
    
    return ans
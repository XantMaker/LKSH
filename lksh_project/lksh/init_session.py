import requests
from . import server

def start():
    qs = server.server + "/post/login"
    requests.post(qs, headers={'Authorization': 'b6d105957c0b5f955bf679f5ba8613fb82a4b883f8418f36a6c8331df4254a40'}, data={"reason":'Я хочу изучать промышленное программирование, не останавливаясь только на спортивном. Несмотря на нулевые знания в этой теме я сделала даже часть ADVENCED уровня(гуглить уже умею).Умею разговаривать и договариваться с окружающими(хорошо работаю в команде)'})
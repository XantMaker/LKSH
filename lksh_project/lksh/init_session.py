import requests
from . import server

def start():
    qs = server.server + "/post/login"
    requests.post(qs, headers={'Authorization': server.auth_str}, data={"reason":'Я хочу изучать промышленное программирование, не останавливаясь только на спортивном. Несмотря на нулевые знания в этой теме я сделала даже часть ADVENCED уровня(гуглить уже умею).Умею разговаривать и договариваться с окружающими(хорошо работаю в команде)'})

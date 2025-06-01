from django.http import HttpResponse

from . import stats_fun
from . import versus_fun
from . import goals_fun
from . import init_session


def index(request):
    return HttpResponse("Hello, Irina Grigoreva LKSH Project index here.")

def stats(request):
    init_session.start()
    ans = stats_fun.stats(request.GET['team_name'])
    return HttpResponse(str(ans[0]) + "     " + str(ans[1]) + "     " + str(ans[2]))

def versus(request):
    init_session.start()
    ans = versus_fun.versus(int(request.GET['player1_id']), int(request.GET['player2_id']))
    return HttpResponse(str(ans))

def goals(request):
    init_session.start()
    
    #ans = request.GET['player_id']
    ans = goals_fun.goals(int(request.GET['player_id']))
    # return HttpResponse("goals"+ans)

    str_ans = "["
    for i in ans:
        str_ans += "{\n" + "\"matches\":" + str(i[0]) + "\n" + "\"time\":" + str(i[1]) + "\n" + "}\n"
    str_ans += "]"

    return HttpResponse(str_ans)

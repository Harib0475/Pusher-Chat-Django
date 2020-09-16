from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher

pusher = Pusher(
    app_id='1074046',
    key='3915806f9a7fb108e5a7',
    secret='8dcc653b00346da5c879',
    cluster='us3',
    ssl=True
)


@login_required(login_url='/admin/login/')
def chat(request):
    return render(request, "chat.html")


@csrf_exempt
def broadcast(request):
    pusher.trigger('a_channel', 'an_event', {'name': request.user.username, 'message': request.POST['message']})
    return HttpResponse("done")

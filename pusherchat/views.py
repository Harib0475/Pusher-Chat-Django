from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher

pusher = Pusher(
    app_id='YOUR_APP_ID',
    key='YOUR_APP_KEY',
    secret='YOUR_APP_SECRET',
    cluster='YOUR_CLUSTER',
    ssl=True
)


@login_required(login_url='/admin/login/')
def chat(request):
    return render(request, "chat.html")


@csrf_exempt
def broadcast(request):
    pusher.trigger('a_channel', 'an_event', {'name': request.user.username, 'message': request.POST['message']})
    return HttpResponse("done")

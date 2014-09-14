from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from app.models import Vote
import socket


def index(request):
    votes = Vote.objects.all().order_by('-date')
    return render(request, 'index.html', {'votes': votes})


@csrf_protect
def vote_next(request):
    ip = request.META.get('REMOTE_ADDR')

    if Vote.objects.filter(ip=ip).count() > 0:
        messages.add_message(request, messages.ERROR, 'You have already voted.')
        return redirect('app.views.index')

    reverse = socket.gethostbyaddr(ip)[0]
    vote = Vote(ip=ip, reverse=reverse, point=1)
    vote.save()
    messages.add_message(request, messages.SUCCESS, 'You have successfully voted.')
    return redirect('app.views.index')


@csrf_protect
def vote_keep(request):
    ip = request.META.get('REMOTE_ADDR')

    if Vote.objects.filter(ip=ip).count() > 0:
        messages.add_message(request, messages.ERROR, 'You have already voted.')
        return redirect('app.views.index')

    reverse = socket.gethostbyaddr(ip)[0]
    vote = Vote(ip=ip, reverse=reverse, point=-1)
    vote.save()
    messages.add_message(request, messages.SUCCESS, 'You have successfully voted.')
    return redirect('app.views.index')

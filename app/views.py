from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from app.models import Vote, Client
from lib.spotify import next as spotify_next
import socket


def index(request):
    votes = Vote.objects.all().order_by('-date')
    clients = Client.objects.all().order_by('name')
    c = {
        'votes': votes,
        'clients': clients,
        'mode': settings.MODE,
    }
    return render(request, 'index.html', c)


@csrf_protect
def vote_next(request):
    ip = request.META.get('REMOTE_ADDR')

    try:
        vote = Vote.objects.get(ip=ip)
    except Vote.DoesNotExist:
        try:
            reverse = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            reverse = u'unknown <%s>' % ip

        vote = Vote(ip=ip, reverse=reverse)

    vote.point = 1
    vote.save()

    # test
    votes = Vote.objects.all()
    points = sum(vote.point for vote in votes)

    if settings.MODE == 'static' and points >= settings.STATIC_THRESHOLD:
        spotify_next()
    elif settings.MODE == 'dynamic':
        clients = Client.objects.filter(up=True).count()
        if points >= clients // 2:
            spotify_next()
        else:
            messages.add_message(request, messages.SUCCESS, 'You have successfully voted.')
    else:
        messages.add_message(request, messages.SUCCESS, 'You have successfully voted.')

    return redirect('app.views.index')


@csrf_protect
def vote_keep(request):
    ip = request.META.get('REMOTE_ADDR')

    try:
        vote = Vote.objects.get(ip=ip)
    except Vote.DoesNotExist:
        try:
            reverse = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            reverse = u'unknown <%s>' % ip

        vote = Vote(ip=ip, reverse=reverse)

    vote.point = -1
    vote.save()

    messages.add_message(request, messages.SUCCESS, 'You have successfully voted.')
    return redirect('app.views.index')

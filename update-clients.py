#!/usr/bin/env python
import os
import subprocess
import time
import django
from datetime import datetime

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()

from app.models import Client
from django.conf import settings


def run(refresh, verbose=False):
    devnull = open('/dev/null')

    while True:
        clients = []

        for name in settings.DYNAMIC_CLIENTS:
            code = subprocess.call(['ping', '-n', '-c', '1', '-q', name], stdout=devnull, stderr=devnull)
            up = code == 0

            clients.append(Client(name=name, up=up))

        if verbose:
            print('[%s] updating clients :' % datetime.now().strftime('%Y-%m-%d %H:%M'))
            print('\n'.join('  ' + str(client) for client in clients))

        Client.objects.all().delete()
        Client.objects.bulk_create(clients)

        time.sleep(refresh)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Daemon to update the list of clients.')
    parser.add_argument('-r', '--refresh', dest='refresh', type=int, default=settings.DYNAMIC_REFRESH,
                        help='time between each refresh (in seconds)')
    parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False, help='be verbose')
    args = parser.parse_args()

    run(args.refresh, args.verbose)

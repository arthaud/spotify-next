#!/usr/bin/env python3
import subprocess
import time

BLACKLIST = (
    'Universal Music – Childish Gambino',
    'Warner Music – Led Zeppelin',
    'Men expert  – L\'oréal ',
    'The Avener – Fade Out Lines',
    'Denon  – House of Heos',
    'Bose – Electronic In India',
    'Universal Music – Digster Dancefloor',
    'CLIQUER POUR DÉCOUVRIR – Sennheiser MOMENTUM',
    '20th Century Fox – Gone Girl',
    'Sony Music – George Ezra',
    'wanted on voyage – George Ezra',
    'Kiesza aux platines de la playlist Dancefloor de Digster !  – DANCEFLOOR by KIESZA',
    'Ile-de-France – Conseil Régional des Jeunes',
    'Bose – Bloc Party',
)


def window_name():
    try:
        prop = subprocess.check_output(['xprop', '-name', 'Spotify - Linux Preview', 'WM_ICON_NAME'])
        prop = prop.decode('utf8')
        return prop[prop.index('"') + 1:-2]
    except subprocess.CalledProcessError:
        return None


def pulseaudio_mute():
    subprocess.check_call(['pactl', 'set-sink-mute', '0', 'yes'])


def pulseaudio_unmute():
    subprocess.check_call(['pactl', 'set-sink-mute', '0', 'no'])


def run(verbose=False):
    old = None
    muted = False

    while True:
        current = window_name()
        if current.startswith('Spotify - '):
            current = current[10:]

        if not current:
            print('error: spotify window not found.')
            return

        if verbose:
            if current != old:
                print('new music: %s' % current)

        if current in BLACKLIST \
                or '–' not in current \
                or current.split('–')[0].strip() == current.split('–')[1].strip():
            if not muted:
                if verbose:
                    print('advertisement muted')

                pulseaudio_mute()
                muted = True
        else:
            if muted:
                if verbose:
                    print('unmute')

                pulseaudio_unmute()
                muted = False

        old = current
        time.sleep(0.5)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Mute when listening advertisements.')
    parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False, help='Be verbose')
    args = parser.parse_args()

    run(args.verbose)

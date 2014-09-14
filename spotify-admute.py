#!/usr/bin/env python3
import subprocess
import time

BLACKLIST = (
    'Spotify - Spotify – Spotify',
    'Spotify - Spotify  – Spotify',
    'Spotify - J&B – J&B',
    'Spotify - Universal Music – Childish Gambino',
    'Spotify - Warner Music – Led Zeppelin',
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

        if not current:
            print('error: spotify window not found.')

        if verbose:
            if current != old:
                print('new music: %s' % current)

        if current in BLACKLIST:
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

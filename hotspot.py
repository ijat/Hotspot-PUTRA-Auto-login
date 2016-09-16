#!/bin/python3

import sys
import argparse, signal
sys.path.append('modules')
import guiState


def signal_handler(signal, frame):
    print('== Bye! ==')
    exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(
        epilog='Do use GUI version if you\'re unsure. Command line is for experts only. Some commands only supported in Linux',
        prog='Hotspot@UPM Auto Login',
        description='Script that auto/connects to Hotspot@UPM without opening any login page.'
    )

    parser.add_argument('-ng', '--nogui',
                        help='Run this script without GUI. Default GUI version.',
                        action='store_true')
    parser.add_argument('-u', '--user',
                        type=int,
                        nargs='?',
                        default=None,
                        help='Your username')
    parser.add_argument('-p', '--passwd',
                        type=str,
                        nargs='?',
                        default=None,
                        help='Your password')
    parser.add_argument('-r', '--reset',
                        nargs='?',
                        default=None,
                        help='Auto reset interface when there are no connection after 3 times check (LINUX ONLY)')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0.2')

    args = parser.parse_args()

    if args.nogui and args.user and args.passwd:
        guiState.splitState(args.nogui, args)
    else:
        guiState.splitState()
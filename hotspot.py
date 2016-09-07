#!/bin/python3

import sys, argparse
sys.path.append('modules')
import login, guiState

if __name__ == '__main__':
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
                        help='Your username')
    parser.add_argument('-p', '--pass',
                        type=str,
                        nargs='?',
                        help='Your password')
    parser.add_argument('-r', '--reset',
                        nargs='?',
                        help='Auto reset interface when there are no connection after 3 times check (LINUX ONLY)')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0.2')

    args = parser.parse_args()

    if args.nogui:
        guiState.splitState(args.nogui, args)
    else:
        guiState.splitState()


# user = login.HotspotUPM("172205", "bonbon")
# user.connect()

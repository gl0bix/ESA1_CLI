#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'schellenberg'

__doc__ = """\
Usage:
  recorder.py -l | --list
  recorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
  recorder.py -h | --help

Options:
  -h --help             Show this screen.
  --filename=<name>     Name of recording [default: record.mp3].
  --duration=<time>     Duration of recording in seconds [default: 10].
  --blocksize=<size>   Block size for read/write in bytes [default: 1024].
  -l --list             List all recordings.
  
Info:
  examples for internet radio stations: https://wiki.ubuntuusers.de/Internetradio/Stationen/
"""

import os
from os import listdir
from os.path import isfile, join

from docopt import docopt

from record import record

if __name__ == '__main__':
    args = docopt(__doc__, version='cli_recorder 0.1')
    path = os.path.dirname(__file__)
    print(args)

    if args['<url>'] is not None:
        record(url=args['<url>'],
               filename=args['--filename'],
               blocksize=int(args['--blocksize']),
               duration=int(args['--duration']))

    if args.get('--list'):
        files = [f for f in listdir(path) if isfile(join(path, f)) and f[-4:] == '.mp3']
        print(*files)



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
  --duration=<time>     Duration of recording in seconds [default: 30].
  --blocksize=<size>   Block size for read/write in bytes [default: 300].
  -l --list             List all recordings.
"""

import datetime as dt
import os
import urllib.request as rq

from os import listdir
from os.path import isfile, join
from docopt import docopt


def record(url='http://radios.rtbf.be/musiq3-128.mp3', filename='record.mp3', blocksize=64, duration=30):
    r = rq.urlopen(url)
    start = dt.datetime.now()

    with open(filename, 'wb') as f:
        while (dt.datetime.now() - start).seconds < duration:
            f.write(r.read(blocksize))


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



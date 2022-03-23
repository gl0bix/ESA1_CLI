#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

__author__ = 'schellenberg'

__doc__ = """\
Usage:
  recorder.py 
  recorder.py -l | --list
  recorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
  recorder.py -h | --help

Options:
  -h --help             Show this screen.
  --filename=<name>     Name of recording [default: record.mp3].
  --duration=<time>     Duration of recording in seconds [default: 30].
  --block_size=<size>    Block size for read/write in bytes [default:64].
  -l --list             List all recordings.
"""

import datetime as dt
import urllib.request as rq

from docopt import docopt


def record(url='http://radios.rtbf.be/musiq3-128.mp3', filename='record.mp3', blocksize=64, duration=30):
    r = rq.urlopen(url)
    start = dt.datetime.now()

    with open(filename, 'wb') as f:
        while (dt.datetime.now() - start).seconds < duration:
            f.write(r.read(blocksize))


if __name__ == '__main__':
    args = docopt(__doc__, version='cli_recorder 0.1')

    record(url=args['<url>'], filename=args['--filename'], blocksize=args['--blocksize'])

    print(args)

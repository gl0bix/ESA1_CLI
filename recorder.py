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
  --filename=<name>     Name of recording [default: myRadio].
  --duration=<time>     Duration of recording in seconds [default: 30].
  --block_size=<size>    Block size for read/write in bytes [default:64].
  -l --list             List all recordings.
"""
import requests

from docopt import docopt


def record(url='http://radios.rtbf.be/brf1-128.mp3', filename='record.mp3', blocksize=1024):
    r = requests.get(url, stream=True)

    with open(filename, 'wb') as f:
        try:
            for block in r.iter_content(blocksize):
                f.write(block)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    arguments = docopt(__doc__, version='cli_recorder 0.1')

    record()

    print(arguments)
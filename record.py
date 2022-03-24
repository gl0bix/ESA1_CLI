#!/usr/binPython
# -*- coding: utf-8 -*-

__author__ = 'schellenberg'

import urllib.request as rq
import datetime as dt


def record(url='http://radios.rtbf.be/musiq3-128.mp3', filename='record.mp3', blocksize=64, duration=30):
    r = rq.urlopen(url)
    start = dt.datetime.now()

    with open(filename, 'wb') as f:
        while (dt.datetime.now() - start).seconds < duration:
            f.write(r.read(blocksize))

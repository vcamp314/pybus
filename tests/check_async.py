#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import pybus


def subscriber1(*args):
    print('subscriber 1 received event:')
    time.sleep(2)
    print('sub 1: ' + args[0])


def subscriber2(*args):
    print('subscriber 2 received event:')
    print('sub 2: ' + args[0])


eventbus = pybus.AsyncBus()
eventbus.append(subscriber1)
eventbus.append(subscriber2)
eventbus('test2')

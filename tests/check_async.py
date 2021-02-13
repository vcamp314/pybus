#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import pybus
import asyncio


def subscriber1(q: asyncio.Queue, *args):
    print('subscriber 1 received event:')
    time.sleep(2)
    print('sub 1: ' + args[0])

    print(q.empty())
    print(q.qsize())
    msg = q.get_nowait()
    print(msg)


def subscriber2(q: asyncio.Queue, *args):
    print('subscriber 2 received event:')
    print('sub 2: ' + args[0])
    q.put_nowait('test message from sub1 to sub2')


eventbus = pybus.AsyncBus()
eventbus.append(subscriber1)
eventbus.append(subscriber2)
eventbus('test2')

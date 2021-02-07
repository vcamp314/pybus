import os
import pytest
from .context import pybus

# the below two lines are for pip installing with test option and the tests will open files:
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(CURRENT_DIR)


def subscriber_func(event):
    print('triggered')


def test_bus_add_subscriber():

    eventbus = pybus.Bus()
    eventbus.append(subscriber_func)

    assert subscriber_func in eventbus


def test_bus_remove_subscriber():
    eventbus = pybus.Bus()
    eventbus.append(subscriber_func)
    eventbus.remove(subscriber_func)

    assert subscriber_func not in eventbus

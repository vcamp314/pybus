"""
This is a very simple implementation of a asynchronous event bus.

"""
import threading
import asyncio
from .bus import Bus


class AsyncBus(Bus):
    """Asynchronous event bus.

    subclass of list, conceptually representing a list of the event
    subscribers which are callable objects within individual threads.

    Events can be of any data type and can be fired by calling the
    event bus instance, passing the event into the list as a param.

    subscribers will trigger asynchronously.

    example usage:
    >>> import time
    >>> aysncbus = AsyncBus()
    >>> def subscriber1(*args):
    ...     print('subscriber 1 received event:')
    ...     time.sleep(1)
    ...     print('sub 1: ' + args[0])
    >>> aysncbus.append(subscriber1)
    >>> def subscriber2(*args):
    ...     print('subscriber 2 received event:')
    ...     print('sub 2: ' + args[0])
    >>> aysncbus.append(subscriber2)
    >>> aysncbus('test1')
    subscriber 1 received event:
    subscriber 2 received event:
    sub 2: test1
    sub 1: test1
    """

    def __init__(self):
        self.data_queue = asyncio.Queue()
        super()

    def __call__(self, *args, **kwargs):
        for subscriber in self:
            subscriber_thread = threading.Thread(
                target=subscriber,
                args=(*args, kwargs)
            )
            subscriber_thread.start()
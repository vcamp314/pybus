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

    Attributes
    ----------
    # todo: add inter-thread communication functionailty
    data_queue: asyncio.Queue
        queue of data for use in providing inter-thread communication

    example usage:
    >>> import time
    >>> asyncbus = AsyncBus()
    >>> def subscriber1(q, *args):
    ...     print('subscriber 1 received event:')
    ...     time.sleep(1)
    ...     print('sub 1: ' + args[0])
    >>> asyncbus.append(subscriber1)
    >>> def subscriber2(q, *args):
    ...     print('subscriber 2 received event:')
    ...     print('sub 2: ' + args[0])
    >>> asyncbus.append(subscriber2)
    >>> asyncbus('test1') # doctest: +SKIP
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
                args=(self.data_queue, *args, kwargs)
            )
            subscriber_thread.start()

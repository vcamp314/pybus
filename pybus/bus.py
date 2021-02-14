"""
This is a very simple implementation of a event bus.

Source:
Longpoke's post on SO:
https://stackoverflow.com/questions/1092531/event-system-in-python

"""


class Bus(list):
    """Event bus.

    subclass of list, conceptually representing a list of the event
    subscribers which are callable objects.
    Events can be of any data type and can be fired by calling the
    event bus instance, passing the event into the list as a param.

    example usage:
    >>> eventbus = Bus()
    >>> def subscriber1(x):
    ...     print('subscriber 1 received event:')
    ...     print(x)
    >>> eventbus.append(subscriber1)
    >>> eventbus('test1')
    subscriber 1 received event:
    test1
    >>> def subscriber2(x):
    ...     print('subscriber 2 received event:')
    ...     print(x)
    >>> eventbus.append(subscriber2)
    >>> eventbus('test2')
    subscriber 1 received event:
    test2
    subscriber 2 received event:
    test2
    >>> eventbus.remove(subscriber1)
    >>> eventbus('test3')
    subscriber 2 received event:
    test3
    """

    def __call__(self, *args, **kwargs):
        for subscriber in self:
            subscriber(*args, **kwargs)

    def __repr__(self):
        return "Bus(%s)" % list.__repr__(self)

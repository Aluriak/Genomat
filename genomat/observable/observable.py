# -*- coding: utf-8 -*-
#########################
#       OBSERVABLE      #
#########################
"""
Definition of an observable.
"""

#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################


class Observable():
    """
    Keep a list of observer, with an update method that is called when necessary.
    This is something like an abstract class.
    """

    def __init__(self, observers=None):
        self.observers = observers if observers is not None else []
    def attach_observer(self, new_observer):
        self.observers.append(new_observer)
    def detach_observer(self, observer):
        self.observers.remove(observer)
    def notify_observers(self, *args, **kwargs):
        [o.update(*args, **kwargs) for o in self.observers]
    def finalize_observers(self):
        [o.finalize(self) for o in self.observers]


#########################
# FUNCTIONS             #
#########################




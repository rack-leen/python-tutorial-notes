#!/usr/bin/env python
# coding=utf-8
class Error(Exception):
    """
    Base clase for Exceptions in this moudle.
    """
    pass

class InputError(Error):
    """
    Exception raised for errors in the input .
    Attributes:
        exception -- input expression in which the error occured
        message -- explanation of the error
    """
    def __init__(self,expression,message): #self是指向类的实例（根据类创建出的具象化对象）
        self.expression = expression #self实例的expression方法
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

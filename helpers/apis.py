from enum import Enum

from stackapi import StackAPI


class Api(object):
    __instance = {}

    def __init__(self, source):
      """ Virtually private constructor. """
      if self.__instance[source] != None:
         raise Exception("This class is a singleton!")
      else:
          if self.__Api[source] == self.__API.stackoverflow:
              self.__instance[source] = StackAPI('stackoverflow')


    @classmethod
    def get_instance(cls, source):
        return cls.__instance[source]


    class __API(Enum):
        stackoverflow = "stackoverflow"

        def __str__(self):
            return self.value

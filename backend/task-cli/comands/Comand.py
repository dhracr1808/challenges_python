from abc import ABC, abstractmethod


class AbstractComand(ABC):
    @abstractmethod
    def execute(self):
        pass


class ComandTask(AbstractComand):
    def __init__(self, comand):
        self.__accion = comand

    def execute(self, *args):
        self.__accion(*args)

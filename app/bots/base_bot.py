from abc import ABC, abstractmethod

class BaseBot(ABC):

    @abstractmethod
    def run(self):
        pass
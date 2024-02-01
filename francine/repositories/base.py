from abc import ABC, abstractmethod


class BaseRepostitory(ABC):
    @abstractmethod
    def add(self, obj: object):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        raise NotImplementedError

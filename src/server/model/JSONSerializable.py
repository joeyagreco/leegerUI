from abc import ABC, abstractmethod


class JSONSerializable(ABC):
    """
    Models should implement this to be JSON serializable.
    """

    @staticmethod
    @abstractmethod
    def to_json(self):
        ...

from abc import ABC, abstractmethod


class JSONDeserializable(ABC):
    """
    Models should implement this to be JSON deserializable.
    """

    @staticmethod
    @abstractmethod
    def from_json(d: dict):
        ...

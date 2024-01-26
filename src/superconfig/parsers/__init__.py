from abc import ABC, abstractmethod


class BaseParser:
    @abstractmethod
    def read(self, path: str):
        pass

    @abstractmethod
    def validate_key(self, key: str):
        pass

    @abstractmethod
    def get(self, key: str):
        pass

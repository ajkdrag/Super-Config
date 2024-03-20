from abc import ABC, abstractmethod
from typing import Any

import smart_open


class BaseParser:
    data: Any = None

    def __init__(self, path: str, **kwargs):
        raw = self.read(path, **kwargs)
        self.load(raw)

    def read(self, path: str, **kwargs):
        with smart_open.open(path, transport_params=kwargs) as f:
            return f.read()

    @abstractmethod
    def load(self, raw: str):
        pass

    @abstractmethod
    def validate_key(self, key: str):
        pass

    @abstractmethod
    def get(self, key: str):
        pass

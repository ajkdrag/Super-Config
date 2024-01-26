import os

from superconfig.parsers import BaseParser


class EnvParser(BaseParser):
    def __init__(self, env_prefix: str = ""):
        self.env_prefix = env_prefix

    def read(self, path: str):
        pass

    def validate_key(self, key: str):
        return True

    def _get_canonical_key(self, key: str):
        tokens = [self.env_prefix] if self.env_prefix else []
        tokens += key.split(".")
        return "_".join(tokens)

    def get(self, key: str):
        if self.validate_key(key):
            canonical_key = self._get_canonical_key(key)
            return os.getenv(canonical_key)

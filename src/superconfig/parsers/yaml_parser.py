import yaml

from superconfig.parsers import BaseParser


class YamlParser(BaseParser):
    def __init__(self, path: str):
        self.data = self.read(path)

    def read(self, path: str):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def validate_key(self, key: str):
        return True

    def get(self, key: str):
        if self.validate_key(key):
            keys = key.split(".")
            data = self.data
            for k in keys:
                data = data[k]
            return data

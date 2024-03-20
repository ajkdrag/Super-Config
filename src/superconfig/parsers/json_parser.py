import json

from superconfig.parsers import BaseParser


class JsonParser(BaseParser):
    def load(self, raw: str):
        self.data = json.loads(raw)

    def validate_key(self, key: str):
        return True

    def get(self, key: str):
        if self.validate_key(key):
            keys = key.split(".")
            data = self.data
            for k in keys:
                data = data[k]
            return data

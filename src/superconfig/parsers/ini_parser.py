import configparser

from superconfig.parsers import BaseParser


class IniParser(BaseParser):
    def load(self, raw: str):
        parser = configparser.ConfigParser()
        parser.read_string(raw)
        self.data = parser

    def validate_key(self, key: str):
        num_fields = len(key.split("."))
        return num_fields == 2

    def get(self, key: str):
        if self.validate_key(key):
            section, option = key.split(".")
            return self.data.get(section, option, fallback=None)

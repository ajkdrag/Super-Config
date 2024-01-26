import configparser

from superconfig.parsers import BaseParser


class IniParser(BaseParser):
    def __init__(self, path: str):
        self.parser = configparser.ConfigParser()
        self.read(path)

    def read(self, path: str):
        self.parser.read(path)

    def validate_key(self, key: str):
        num_fields = len(key.split("."))
        return num_fields == 2

    def get(self, key: str):
        if self.validate_key(key):
            section, option = key.split(".")
            return self.parser.get(section, option, fallback=None)

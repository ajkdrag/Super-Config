import os
from pathlib import Path

from superconfig.utilities.dtypes import STR
from superconfig.utilities.parser_utils import get_env_parser, get_file_parser


class SuperConfig:
    _parsers = []
    KEY_NOT_FOUND = object

    @staticmethod
    def setup(path_default: str, path_custom: str, env_prefix=""):
        SuperConfig._env_prefix = "" if env_prefix is None else env_prefix
        SuperConfig._parsers = [
            get_env_parser(env_prefix),
            get_file_parser(path_custom),
            get_file_parser(path_default),
        ]

    @staticmethod
    def get(key: str, fallback: object = KEY_NOT_FOUND, dtype: STR = STR):
        for parser in SuperConfig._parsers:
            try:
                res = parser.get(key)
                if res is not None:
                    return dtype(res)
            except KeyError:
                pass
        if fallback == SuperConfig.KEY_NOT_FOUND:
            raise KeyError(f"Value for {key} not found.")
        return fallback

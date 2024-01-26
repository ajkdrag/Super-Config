from typing import Union

from superconfig.parsers.env_parser import EnvParser
from superconfig.parsers.ini_parser import IniParser
from superconfig.parsers.json_parser import JsonParser
from superconfig.parsers.yaml_parser import YamlParser


def get_env_parser(env_prefix: str = "") -> EnvParser:
    return EnvParser(env_prefix)


def get_file_parser(path_to_file: str) -> Union[IniParser, JsonParser, YamlParser]:
    file_type = path_to_file.split(".")[-1]
    if file_type == "ini":
        return IniParser(path_to_file)
    elif file_type == "json":
        return JsonParser(path_to_file)
    elif file_type == "yaml":
        return YamlParser(path_to_file)
    raise NotImplementedError(f"File type {file_type} not supported.")

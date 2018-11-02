import yaml
import json
import os

from exception.exception import ConfigDoesNotExist


def parse_yaml(dir: str, name: str) -> dict:
    """
    Parse .yaml files for content.
    :param dir: <str> directory name of the yaml-file
    :param name: <str> yaml-filename
    :return: <dict> content of the yaml-file
    """
    assert name.lower().endswith('.yaml'), f'File-type exception. It has to be a `.yaml` , but {name} received'
    return _parse(dir, name, yaml.load)


def parse_json(dir: str, name: str) -> dict:
    """
    Parse .json file by path
    :param dir: <str> directory name of the json-file
    :param name: <str> json-filename
    :return: <dict> file content
    """
    assert name.lower().endswith('.json'), f'File-type exception. It has to be a `.json` , but {name} received'
    return _parse(dir, name, json.load)


def _parse(dir: str, name: str, load) -> dict:
    """
    Parse any file by path
    :param dir: <str> directory name of the file
    :param name: <str> filename
    :param load: load func to read current file
    :return: <dict> file conten
    """
    path = os.path.join(dir, name) if dir else name
    with open(path) as f:
        try:
            return load(f)
        except FileNotFoundError:
            raise ConfigDoesNotExist(path)

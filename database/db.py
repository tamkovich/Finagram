import sqlalchemy as sa
import json


CONFIG = {
    'filepath': 'database/config.json',
    'type': 'json'
}


def load_config_json(filepath: str):
    """
    load .json file by filepath
    :param filepath: path to file, from executed program
    :return: <dict> file content
    """
    assert filepath.endswith('.json'), f'File-type exception. ' \
                                       f'It has to be a `.json` , but {filepath} received'
    with open(filepath) as f:
        return json.load(f)


def load_engine(echo: bool=False):
    """
    create database engine from config-file params
    :param echo: bool flag. param for sqlalchemy.create_engine func.
    :return: [sqlalchemy] engine
    """
    config = dict()
    if CONFIG['type'] == 'json':
        config = load_config_json(CONFIG['filepath'])
    else:
        pass
    database = "mysql://{0}:{1}@{2}/{3}".format(
        config['user'], config['password'], config['host'], config['database']
    )
    return sa.create_engine(database, echo=echo)

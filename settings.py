from private.parse_config import parse

config = dict()
config['app'] = parse('private', 'config.yaml')

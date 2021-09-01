import configparser

config = configparser.ConfigParser()

config.read('config.ini')

database = dict(config['Mysql'])

telegram = dict(config['Telegram'])
#!/usr/bin/env python3

import configparser
import os
from pathlib import Path


class Config:

    SECTION = 'GitHub'
    CONFIG_ROOT = os.environ.get("XDG_CONFIG_HOME", os.path.join(os.environ.get("HOME"), ".config"))
    CONFIG_PATH = Path(CONFIG_ROOT) / "ghnotifier"

    DEFAULT_REFRESH_TIME = 30

    def __init__(self):
        self.config_file_path = self.CONFIG_PATH / 'config.ini'
        self.configParser = configparser.ConfigParser()
        self.configParser['DEFAULT'] = {'refreshTime': self.DEFAULT_REFRESH_TIME, 'accesstoken': ''}
        self.configParser[self.SECTION] = {}
        self.refresh()

    def get(self, name):
        return self.configParser.get(self.SECTION, name)

    def has(self, name):
        return self.configParser.has_option(self.SECTION, name) and self.configParser.get(self.SECTION, name)

    def set(self, name, value):
        self.configParser.set(self.SECTION, name, value)

    def update(self):
        self.CONFIG_PATH.mkdir(exist_ok=True, parents=True)
        self.configParser.write(open(self.config_file_path, 'w'))

    def refresh(self):
        self.configParser.read(self.config_file_path)

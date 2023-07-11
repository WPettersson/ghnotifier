#!/usr/bin/env python3

from importlib.resources import files

import gi

gi.require_version('AyatanaAppIndicator3', '0.1')

from gi.repository import AyatanaAppIndicator3 as appindicator, GObject
from ghnotifier.config import Config


class Indicator:

    INDICATOR_ID = 'Github Notifier'
    ICON_PATH = files("ghnotifier").joinpath("gh.png")

    def __init__(self):
        self.indicator = appindicator.Indicator.new(
            self.INDICATOR_ID,
            str(self.ICON_PATH),
            appindicator.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_label("0", '')

    def set_menu(self, menu):
        self.indicator.set_menu(menu)

    def update_label(self, label):
        GObject.idle_add(
            self.indicator.set_label,
            label, '',
            priority=GObject.PRIORITY_DEFAULT
        )

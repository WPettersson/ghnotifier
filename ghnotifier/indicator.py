#!/usr/bin/env python3

from enum import Enum
from importlib.resources import files

import gi

gi.require_version('AyatanaAppIndicator3', '0.1')

from gi.repository import AyatanaAppIndicator3 as appindicator, GObject
from ghnotifier.config import Config


class IndicatorStatus(Enum):
    PASSIVE = appindicator.IndicatorStatus.PASSIVE
    ACTIVE = appindicator.IndicatorStatus.ACTIVE
    ATTENTION = appindicator.IndicatorStatus.ATTENTION


class Indicator:

    INDICATOR_ID = 'Github Notifier'
    ICON_PATH = files("ghnotifier").joinpath("gh.png")
    ICON_PATH_ATTENTION = files("ghnotifier").joinpath("gh-attention.png")


    def __init__(self):
        self.indicator = appindicator.Indicator.new(
            self.INDICATOR_ID,
            str(self.ICON_PATH),
            appindicator.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_label("0", '')
        self.indicator.set_icon(str(self.ICON_PATH))
        self.indicator.set_attention_icon(str(self.ICON_PATH_ATTENTION))

    def set_menu(self, menu):
        self.indicator.set_menu(menu)

    def update_label(self, label):
        GObject.idle_add(
            self.indicator.set_label,
            label, '',
            priority=GObject.PRIORITY_DEFAULT
        )

    def set_status(self, status):
        match status:
            case IndicatorStatus.PASSIVE:
                self.indicator.set_status(appindicator.IndicatorStatus.PASSIVE)
                return
            case IndicatorStatus.ACTIVE:
                self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
                self.indicator.set_icon(str(self.ICON_PATH))
                self.indicator.set_attention_icon(str(self.ICON_PATH))
                return
            case IndicatorStatus.ATTENTION:
                self.indicator.set_status(appindicator.IndicatorStatus.ATTENTION)
                self.indicator.set_attention_icon(str(self.ICON_PATH_ATTENTION))
                return

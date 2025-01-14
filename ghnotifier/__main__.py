#!/usr/bin/env python


def run_gui():
    import signal
    import gi

    gi.require_version('Gtk', '3.0')
    gi.require_version('AyatanaAppIndicator3', '0.1')
    gi.require_version('Notify', '0.7')

    from gi.repository import Gtk, GObject
    from ghnotifier.notifier import Notifier
    from ghnotifier.indicator import Indicator
    from threading import Thread
    from ghnotifier.menu import Menu


    indicator = Indicator()
    indicator.set_menu(Menu().get_inner())
    notifier = Notifier(indicator)

    thread = Thread(target=notifier.notify)
    thread.daemon = True
    thread.start()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == "__main__":
    run_gui()

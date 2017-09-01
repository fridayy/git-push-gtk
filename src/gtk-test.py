import gi
import os
import sys
from subprocess import check_output, CalledProcessError, run

gi.require_version('Notify', '0.7')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Notify

class Notification(Gtk.Window):
    """
    Represents a GTK Notification
    """
    def show_notification(self, title, message):
        Notify.init('notify')
        notification = Notify.Notification.new(title, message)
        notification.set_timeout(10000)
        notification.show()


if len(sys.argv) == 2:
    win = Notification()
    try:
        check_output(["git", "add", "-A", "."])
        check_output(["git", "commit", "-m", str(sys.argv[1])])
        run(["git", "push"])
        win.show_notification("Success!", "Successfully pushed: {}".format(os.getcwd()))
    except CalledProcessError as e:
        win.show_notification("Error!", "<b>{}</b>".format(e.__str__()))

else:
    print("Commit Message required!")
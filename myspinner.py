import gtk
import subprocess
import time

class MySpinner:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file('ui/spinner.ui')
        self.pref_window = self.builder.get_object("spinnerw")
        #self.close_button = self.builder.get_object("close_button")
        #self.close_button.connect('clicked', self.onPluginCloseButton)

        self.builder.connect_signals(self)
        self.pref_window.show_all()

    def open_snep_server(self, widget):
        print "Opening snep server..."

        cmd = 'sudo timeout 3s /home/pi/explore-nfc/poll/card_polling/build/card_polling'
        subprocess.call(cmd, shell=True)

        cmd = 'sudo /home/pi/explore-nfc/p2p/P2P-SNEP_clientPUT/build/Snep_client'
        subprocess.call(cmd, shell=True)

        while gtk.events_pending():
            gtk.main_iteration()
            gtk.main_iteration()


    #def onPluginCloseButton(self, widget):
    #    self.pref_window.destroy()
    #    self.pref_window = None

    #def on_preferences_window_destroy(self, window):
    #    self.window = None

    #def on_close_button_clicked(self, button):
    #    self.close_window()

    #def on_close(self, widget, event):
    #    self.close_window()


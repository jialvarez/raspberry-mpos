import gtk
import subprocess
import time
import threading
import gobject
import glib

class MySpinner:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file('ui/spinner.ui')
        self.pref_window = self.builder.get_object("spinnerw")
        self.spinner = self.builder.get_object("spinner1")
        #self.close_button = self.builder.get_object("close_button")
        #self.close_button.connect('clicked', self.onPluginCloseButton)

        self.builder.connect_signals(self)
        self.pref_window.show_all()

    def open_snep_server(self, spinner, finishcb):
        print "Opening snep server..."
        spinner.show()
        spinner.start()

        def thread_run():
            # call heavy here
            cmd = 'sudo timeout 3s /home/pi/explore-nfc/poll/card_polling/build/card_polling'
            #subprocess.call(cmd, shell=True)

            cmd = 'sudo /home/pi/explore-nfc/p2p/P2P-SNEP_clientPUT/build/Snep_client'
            #subprocess.call(cmd, shell=True)
            gobject.idle_add(cleanup, cmd)

        def cleanup(cmd):
            print "cleaning up"
            spinner.stop()
            spinner.hide()
            t.join()
            finishcb(cmd)
            print "Stopping snep server..."

        # start "heavy" in a separate thread and immediately
        # return to mainloop
        t = threading.Thread(target=thread_run)
        t.start()

    def show_spinner(self, widget):
        self.open_snep_server(self.spinner, self.save_and_quit)

    def save_and_quit(self, mybool):
        print "Sacabo: " + str(mybool)
        self.pref_window.destroy()

    #def onPluginCloseButton(self, widget):
    #    self.pref_window.destroy()
    #    self.pref_window = None

    #def on_preferences_window_destroy(self, window):
    #    self.window = None

    #def on_close_button_clicked(self, button):
    #    self.close_window()

    #def on_close(self, widget, event):
    #    self.close_window()


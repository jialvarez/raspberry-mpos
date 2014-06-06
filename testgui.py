import sys
import gtk
import myspinner
import pluglib
import glib
import gobject

class TestGUI:

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file('ui/testgui.ui')
        self.window = self.builder.get_object('window1')
        self.window.show_all()
        self.builder.connect_signals(self)

    def spinner(self, widget):
        """Display the spinner window."""
        print "Opening spinner..."
        s = myspinner.MySpinner()

    def about(self, widget):
        """Display the about window."""
        authors = ["Nacho Alvarez <nacho@wul4.com>"]
        url = "http://www.wul4.com"

        self.aboutDialog = gtk.AboutDialog()
        self.aboutDialog.set_authors(authors)
        self.aboutDialog.set_name('Raspberry mPOS')
        self.aboutDialog.set_website(url)
        self.aboutDialog.set_title('Raspberry mPOS')
        self.aboutDialog.connect('response', self.aboutDialogOnResponse)
        self.aboutDialog.show()

    def aboutDialogOnResponse(self, dialog, responseID):
        """Signal handler for the About Dialog's "response" signal."""

        dialog.destroy()
        self.aboutDialog = None

    def showPreferences(self, widget):
        if self.preferences:
            return

        p = prefs.Preferences()

    def onPluginCloseButton(self, widget):
        self.preferences.destroy()
        self.preferences = None

    def onDestroy(self, widget):
        gtk.main_quit()

    def onExitButton(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    v = TestGUI()
    glib.threads_init()
    gtk.main()
    gobject.threads_init()
    sys.exit(0)

import pyinotify
import mediaidentifier
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--loglevel", help="Set the python logging level")
args = parser.parse_args()

class FileHandler(pyinotify.ProcessEvent):
	def process_IN_CLOSE_WRITE(self, event):
		logging.debug("File with path=" + event.path + ", name=" + event.name + " was CLOSE_WRITE'd")
		logging.debug("Is audio file: " + str(ident.identifyAudio(event.name)))

loglevel = getattr(args, "loglevel", "WARNING")
logging.basicConfig(level=loglevel)

logging.info("PyMediaConverter loading. loglevel=" + str(loglevel))

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# process events).

ident = mediaidentifier.MediaIdentifier()

# Add a new watch on /tmp for CLOSE_WRITE events (i.e. when a file is ready to be processed)
wm.add_watch('/tmp', pyinotify.IN_CLOSE_WRITE, rec=True, auto_add=True)
handler = FileHandler()
notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
# Loop forever and handle events.
logging.info("Starting event loop.")
notifier.loop()

import pyinotify

class FileHandler(pyinotify.ProcessEvent):
	def process_IN_CLOSE_WRITE(self, event):
		print("File with name=" + event.name + " was CLOSE_WRITE'd")

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# process events).

# Add a new watch on /tmp for CLOSE_WRITE events (i.e. when a file is ready to be processed)
wm.add_watch('/tmp', pyinotify.IN_CLOSE_WRITE)
handler = FileHandler()
notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
# Loop forever and handle events.
notifier.loop()

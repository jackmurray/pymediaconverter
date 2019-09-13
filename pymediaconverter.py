import pyinotify

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# process events).
notifier = pyinotify.Notifier(wm)
# Add a new watch on /tmp for CLOSE_WRITE events (i.e. when a file is ready to be processed)
wm.add_watch('/tmp', pyinotify.IN_CLOSE_WRITE)
# Loop forever and handle events.
notifier.loop()

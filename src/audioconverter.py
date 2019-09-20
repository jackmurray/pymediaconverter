import time
import mediaconverter

class AudioConverter(mediaconverter.MediaConverter):
	"""Audio conversion class"""
	AUDIO_TARGET_FORMAT = "mp3"
	AUDIO_TARGET_BITRATE = 320

	def convert(self, filename):
		print("fake converting " + filename)
		time.sleep(5)
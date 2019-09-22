import mediaconverter
import subprocess
import logging

class AudioConverter(mediaconverter.MediaConverter):
	"""Audio conversion class"""
	AUDIO_TARGET_FORMAT = ".mp3"
	AUDIO_TARGET_BITRATE = 320

	def convert(self, filename, srcformat):
		logging.info("AudioConverter converting " + filename + " from " + srcformat + " to " + self.AUDIO_TARGET_FORMAT)
		outputfilename = filename.replace(srcformat, self.AUDIO_TARGET_FORMAT)
		subprocess.run(["ffmpeg", "-i", filename, "-b:a", str(self.AUDIO_TARGET_BITRATE)+"k", outputfilename])
		
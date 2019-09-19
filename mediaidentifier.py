class MediaIdentifier:
	"""Class to identify what type of media a file contains by filename."""
	AUDIO_TARGET_FORMAT = "mp3"
	AUDIO_TARGET_BITRATE = 320
	AUDIO_FORMATS = [ ".m4a", ".flac", ".alac" ]

	def identifyAudio(self, filename):
		return any(x in filename for x in self.AUDIO_FORMATS)

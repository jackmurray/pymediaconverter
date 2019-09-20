class MediaIdentifier:
	"""Class to identify what type of media a file contains by filename."""
	AUDIO_FORMATS = [ ".m4a", ".flac", ".alac" ]

	def identifyAudio(self, filename):
		return any(x in filename for x in self.AUDIO_FORMATS)

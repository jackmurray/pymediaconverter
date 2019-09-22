class MediaIdentifier:
	"""Class to identify what type of media a file contains by filename."""
	AUDIO_FORMATS = [ ".m4a", ".flac", ".alac" ]

	def identifyAudio(self, filename):
		for format in self.AUDIO_FORMATS:
			length = len(format)
			substring = filename[-length:] #Get the last x characters of the filename, which should hopefully match an entry from AUDIO_FORMATS
			if substring == format:
				return format
		return False

from abc import ABC, abstractmethod
class MediaConverter(ABC):
	"""Base class for media converters"""
    
	@abstractmethod
	def convert(self, filename, srcformat):
		pass
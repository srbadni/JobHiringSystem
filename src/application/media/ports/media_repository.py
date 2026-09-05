from abc import ABC, abstractmethod

from ..dto import MediaDTO


class MediaRepository(ABC):

    @abstractmethod
    async def add(self, media: MediaDTO) -> MediaDTO:
        pass
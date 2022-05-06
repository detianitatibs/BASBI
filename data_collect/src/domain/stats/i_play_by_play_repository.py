from abc import ABCMeta, abstractclassmethod
from typing import List

from .play_by_play_entity import PlayByPlayEntity


class IPlayByPlayRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, list_play_by_play_entity: List[PlayByPlayEntity]):
        pass

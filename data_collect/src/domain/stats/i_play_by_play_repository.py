from abc import ABCMeta, abstractclassmethod

from .play_by_play_entity import PlayByPlayEntity


class IPlayByPlayRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, play_by_play_entity: PlayByPlayEntity):
        pass

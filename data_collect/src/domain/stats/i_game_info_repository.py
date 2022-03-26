from abc import ABCMeta, abstractclassmethod

from .game_info_entity import GameInfoEntity


class IGameInfoRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, game_info_entity: GameInfoEntity):
        pass

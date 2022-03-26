from abc import ABCMeta, abstractclassmethod

from .box_score_entity import BoxScoreEntithy


class IBoxScoreRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, box_score_entity: BoxScoreEntithy):
        pass

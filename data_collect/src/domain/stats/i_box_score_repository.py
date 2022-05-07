from abc import ABCMeta, abstractclassmethod
from typing import List

from .box_score_entity import BoxScoreEntity


class IBoxScoreRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, list_box_score_entity: List[BoxScoreEntity]):
        pass

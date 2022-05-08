from abc import ABCMeta, abstractclassmethod
from typing import List

from .game_report_entity import GamerReportEntity


class IGameReportRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, schedule_key: int, list_game_report_entity: List[GamerReportEntity]):
        pass

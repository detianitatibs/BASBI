from abc import ABCMeta, abstractclassmethod

from .game_report_entity import GamerReportEntity


class IGameReportRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, game_report_entity: GamerReportEntity):
        pass

from injector import Module, Binder

from src.domain.stats.i_collect_stats_usecase import ICollectStatsUsecase
from src.domain.stats.i_game_info_repository import IGameInfoRepository
from src.domain.stats.i_game_report_repository import IGameReportRepository
from src.domain.stats.i_box_score_repository import IBoxScoreRepository
from src.domain.stats.i_play_by_play_repository import IPlayByPlayRepository
from src.application.stats.collect.collect_stats_interactor import CollectStatsInteractor
from src.adapter.stats.gateway.save_game_info_file import SaveGameInfoFile
from src.adapter.stats.gateway.save_game_report_file import SaveGameReportFile
from src.adapter.stats.gateway.save_box_score_file import SaveBoxScoreFile
from src.adapter.stats.gateway.save_play_by_play_file import SavePlayByPlayFile


class DIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ICollectStatsUsecase, to=CollectStatsInteractor)
        binder.bind(IGameInfoRepository, to=SaveGameInfoFile)
        binder.bind(IGameReportRepository, to=SaveGameReportFile)
        binder.bind(IBoxScoreRepository, to=SaveBoxScoreFile)
        binder.bind(IPlayByPlayRepository, to=SavePlayByPlayFile)

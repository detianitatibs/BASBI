from abc import ABCMeta, abstractclassmethod
from typing import List

from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata
from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata
from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata
from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata


class ICollectStatsUsecase(metaclass=ABCMeta):
    @abstractclassmethod
    def translate_and_save(
        self,
        collect_game_info_inputdata: CollectGameInfoInputdata,
        list_collect_game_report_inputdata: List[CollectGameReportInputdata],
        list_collect_box_score_inputdata: List[CollectBoxScoreInputdata],
        list_collect_play_by_play_inputdata: List[CollectPlayByPlayInputdata]
    ) -> None:
        """取得したデータを加工して出力するユースケース

        Args:
            collect_game_info_inputdata (CollectGameInfoInputdata): GameInfoのインプットデータ
            list_collect_game_report_inputdata (List[CollectGameReportInputdata]): GameRportのインプットデータ
            list_collect_box_score_inputdata (List[CollectBoxScoreInputdata]): BoxScoreのインプットデータ
            list_collect_play_by_play_inputdata (List[CollectPlayByPlayInputdata]): PlayByPlayのインプットデータ
        """
        pass

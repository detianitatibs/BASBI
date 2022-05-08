import os
import csv
import logging
from typing import List

from dataclasses import asdict

from src.domain.stats.i_game_report_repository import IGameReportRepository
from src.domain.stats.game_report_entity import GamerReportEntity

logger = logging.getLogger(__name__)


class SaveGameReportFile(IGameReportRepository):

    def save(self, schedule_key: int,  list_game_report_entity: List[GamerReportEntity]) -> None:
        """GameReportをファイルとして保存する

        Args:
            schedule_key (int): スケジュールキー
            list_game_report_entity (List[GamerReportEntity]): entityのリスト
        """
        # 保存場所の作成
        basbi_path = os.environ['BASBIPATH']
        dir_path = os.path.join(basbi_path, 'data', 'schedule='+str(schedule_key))
        logger.info('save path: {}'.format(dir_path))
        os.makedirs(dir_path, exist_ok=True)
        
        # データをdictに変換する
        list_game_report_dict = [asdict(game_report_entity) for game_report_entity in list_game_report_entity]
        game_report_header = list(list_game_report_dict[0].keys())

        # ファイルとして保存する
        filename = 'game_report_'+ str(schedule_key) + '.tsv'
        with open(os.path.join(dir_path, filename), 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=game_report_header)
            writer.writeheader()
            writer.writerows(list_game_report_dict)
            logger.info('write to {}'.format(filename))

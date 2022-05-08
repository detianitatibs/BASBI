import os
import csv
import logging
from typing import List

from dataclasses import asdict

from src.domain.stats.i_play_by_play_repository import IPlayByPlayRepository
from src.domain.stats.play_by_play_entity import PlayByPlayEntity

logger = logging.getLogger(__name__)


class SavePlayByPlayFile(IPlayByPlayRepository):

    def save(self, schedule_key: int,  list_play_by_play_entity: List[PlayByPlayEntity]) -> None:
        """PlayByPlayをファイルとして保存する

        Args:
            schedule_key (int): スケジュールキー
            list_play_by_play_entity (List[PlayByPlayEntity]): entityのリスト
        """
        # 保存場所の作成
        basbi_path = os.environ['BASBIPATH']
        dir_path = os.path.join(basbi_path, 'data', 'schedule='+str(schedule_key))
        logger.info('save path: {}'.format(dir_path))
        os.makedirs(dir_path, exist_ok=True)
        
        # データをdictに変換する
        list_play_by_play_dict = [asdict(play_by_play_entity) for play_by_play_entity in list_play_by_play_entity]
        play_by_play_header = list(list_play_by_play_dict[0].keys())

        # ファイルとして保存する
        filename = 'play_by_play_'+ str(schedule_key) + '.tsv'
        with open(os.path.join(dir_path, filename), 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=play_by_play_header)
            writer.writeheader()
            writer.writerows(list_play_by_play_dict)
            logger.info('write to {}'.format(filename))

import os
import csv
import logging
from typing import List

from dataclasses import asdict

from src.domain.stats.i_box_score_repository import IBoxScoreRepository
from src.domain.stats.box_score_entity import BoxScoreEntity

logger = logging.getLogger(__name__)


class SaveBoxScoreFile(IBoxScoreRepository):

    def save(self, schedule_key: int,  list_box_score_entity: List[BoxScoreEntity]) -> None:
        """BoxScoreをファイルとして保存する

        Args:
            schedule_key (int): スケジュールキー
            list_box_score_entity (List[BoxScoreEntity]): entityのリスト
        """
        # 保存場所の作成
        basbi_path = os.environ['BASBIPATH']
        dir_path = os.path.join(basbi_path, 'data', 'schedule='+str(schedule_key))
        logger.info('save path: {}'.format(dir_path))
        os.makedirs(dir_path, exist_ok=True)
        
        # データをdictに変換する
        list_box_score_dict = [asdict(box_score_entity) for box_score_entity in list_box_score_entity]
        box_score_header = list(list_box_score_dict[0].keys())

        # ファイルとして保存する
        filename = 'box_score_'+ str(schedule_key) + '.tsv'
        with open(os.path.join(dir_path, filename), 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=box_score_header)
            writer.writeheader()
            writer.writerows(list_box_score_dict)
            logger.info('write to {}'.format(filename))

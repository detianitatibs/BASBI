import os
import csv
import logging

from dataclasses import asdict

from src.domain.stats.i_game_info_repository import IGameInfoRepository
from src.domain.stats.game_info_entity import GameInfoEntity

logger = logging.getLogger(__name__)


class SaveGameInfoFile(IGameInfoRepository):

    def save(self, schedule_key: int,  game_info_entity: GameInfoEntity) -> None:
        """GameInfoをファイルとして保存する

        Args:
            schedule_key (int): スケジュールキー
            game_info_entity (GameInfoEntity): entity
        """
        # 保存場所の作成
        basbi_path = os.environ['BASBIPATH']
        dir_path = os.path.join(basbi_path, 'data', 'schedule='+str(schedule_key))
        logger.info('save path: {}'.format(dir_path))
        os.makedirs(dir_path, exist_ok=True)
        
        # データをdictに変換する
        game_info_dict = asdict(game_info_entity)
        game_info_header = list(game_info_dict.keys())
        
        # ファイルとして保存する
        filename = 'game_info_'+ str(schedule_key) + '.tsv'
        with open(os.path.join(dir_path, filename), 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=game_info_header)
            writer.writeheader()
            writer.writerow(game_info_dict)
            logger.info('write to {}'.format(filename))

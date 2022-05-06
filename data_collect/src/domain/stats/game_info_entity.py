from dataclasses import dataclass
from datetime import date, time
from typing import List


@dataclass(frozen=True)
class GameInfoEntity:
    """試合情報を保持するエンティティ
    """
    schedule_key: int
    game_date: str  # 試合日(YYYY-mm-dd)
    tipoff: str  # 試合開始時間(HH:MM)
    season: str  # 年度
    division: str # カテゴリ(ディビジョン)
    sec: int  # 節
    arena: str  # 会場名
    attendance: int # 観客数
    referee_1: str  # レフェリー1
    referee_2: str  # レフェリー2
    referee_3: str  # レフェリー3
    home_fullname: str  # ホームチーム(フル名称)
    home_name: str  # ホームチーム(略称名)
    home_score: int  # ホームチーム総得点
    home_score_q: List[int]  # ホームチームQ別得点
    away_fullname: str  # アウェイチーム(フル名称)
    away_name: str  # アウェイチーム(略称名)
    away_score: int  # アウェイチーム総得点
    away_score_q: List[int]  # アウェイチームQ別得点

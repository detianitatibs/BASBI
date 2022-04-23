from dataclasses import dataclass
from datetime import date, time
from typing import List


@dataclass(frozen=True)
class CollectGameInfoInputdata:
    """スクレイピングから取得した試合情報
    """
    schedule_key: int
    title: str # ページのタイトル(20YY-YY BXリーグ YYYY/mm/dd Home VS Away - B.LEAGUE（Bリーグ）公式サイト)
    tipoff: str  # 試合開始時間(HH:MM TIP OFF)
    sec: str  # 節(第X節)
    arena: str  # 会場名(会場：XXXX)
    attendance: str # 観客数(人数：XXXX人)
    referee: str # レフェリー名(レフェリー：XX　XX／XX　XX／XX　XX)
    home_fullname: str  # ホームチーム(フル名称)
    home_name: str  # ホームチーム(略称名)
    away_fullname: str  # アウェイチーム(フル名称)
    away_name: str  # アウェイチーム(略称名)
    home_score: int  # ホームチーム総得点
    home_score_q: List[int]  # ホームチームQ別得点
    away_score: int  # アウェイチーム総得点
    away_score_q: List[int]  # アウェイチームQ別得点

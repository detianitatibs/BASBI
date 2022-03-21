from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class PlayByPlayEntity:
    """Play-by-playを保持するエンティティ
    """
    schedule_key: int
    data_no: int # 何行目のテキストかを示す
    action_cd: str # どういったアクションなのかを判別するコード
    home_away: str  # ホームアウェイ区分(H, A) ※data_classから判別
    period: str # 何ピリオドかを示す
    time_remaining: time # 残り時間
    flg_point: bool # ポイントを取ったテキストの場合はTrue
    point_home: int # flg_pointがTrueのときのhomeの点数、FalseのときはNone
    point_away: int # flg_pointがTrueのときのawayの点数、FalseのときはNone
    details: str # テキスト詳細

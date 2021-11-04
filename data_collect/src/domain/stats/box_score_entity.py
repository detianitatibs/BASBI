from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class BoxScoreEntithy:
    """ボックススコア
    """
    schedule_key: int
    home_away: str  # ホームアウェイ区分
    team_name: str  # チーム(略称名)
    no: int  # 背番号
    player_id: int  # プレイヤーID
    player_name: str  # 選手名
    quoter: str  # クォーターカテゴリ
    start_flg: bool  # スターティングフラグ
    position: str  # ポジション
    minutes: time  # 出場時間(MM:SS)
    pts: int  # Total Points
    fgm: int  # 2 Points FGM (成功数)
    fga: int  # 2 Points FGA (試行数)

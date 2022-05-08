from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class BoxScoreEntity:
    """ボックススコア
    """
    schedule_key: int
    home_away: str  # ホームアウェイ区分(H, A)
    team_name: str  # チーム
    no: int  # 背番号
    player_id: int  # プレイヤーID
    player_name: str  # 選手名(全角空白は半角空白に変換する)
    quoter: str  # クォーターカテゴリ(ALL, 1Q, 2Q, 3Q, 4Q, EX1...)
    start_flg: bool  # スターティングフラグ
    position: str  # ポジション
    minutes: str  # 出場時間(MM:SS)
    pts: int  # Total Points
    fgm: int  # 2 Points FGM (成功数)
    fga: int  # 2 Points FGA (試行数)
    fgr: float  # 2 Points FGR (成功数/試行数)
    fgm3: int  # 3 Points FGM
    fga3: int # 3 Points FGA
    fgr3: float  # 3 Points FGR
    ftm: int  # Free-ThrowsM
    fta: int  # Free-ThrowsA
    ftr: float  # Free-ThrowsR
    ofr: int  # Offensive Rebounds
    der: int  # Defensive Rebounds
    tor: int  # Total Rebounds
    ast: int  # Assist
    to: int  # TurnOver
    st: int  # Steals
    bo: int  # Blocks
    bsr: int  # 被Blocks
    fo: int  # Fouls
    fd: int  # 被Fouls
    dunk: int  # Dunks
    eff: float  # EFF

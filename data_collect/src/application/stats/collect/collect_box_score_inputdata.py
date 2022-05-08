from dataclasses import dataclass


@dataclass(frozen=True)
class CollectBoxScoreInputdata:
    """スクレイピンから取得したBOX SCORE情報
    """
    schedule_key: int
    home_away: str  # ホームアウェイ区分(H, A)
    team_name: str  # チーム
    quoter: str  # クォーターカテゴリ(0:ALL, 1:1Q, 2:2Q, 3:3Q, 4:4Q...)
    player_id: str  # プレイヤーID
    no: str  # 背番号
    start_flg: str  # スターティングフラグ('〇'/'')
    player_name: str  # 選手名
    position: str  # ポジション
    minutes: str  # 出場時間(MM:SS)
    pts: int  # Total Points
    fgm: int  # 2 Points FGM (成功数)
    fga: int  # 2 Points FGA (試行数)
    fgr: str  # 2 Points FGR (成功数/試行数)
    fgm3: int  # 3 Points FGM
    fga3: int # 3 Points FGA
    fgr3: str  # 3 Points FGR
    ftm: int  # Free-ThrowsM
    fta: int  # Free-ThrowsA
    ftr: str  # Free-ThrowsR
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

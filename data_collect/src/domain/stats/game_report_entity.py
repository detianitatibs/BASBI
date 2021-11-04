from dataclasses import dataclass


@dataclass(frozen=True)
class GamerReportEntity:
    """試合レポートを保持するエンティティ
    """
    schedule_key: int
    home_away: str  # ホームアウェイ区分
    team_name: str  # チーム(略称名)
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
    fo: int  # Fouls
    fbp: int  # First Break Points
    bl: int  # Biggest Lead
    pp: int  # Points in the Paint
    pto: int  # Point From Turnover
    scp: int  # Secound Chance Points
    bsr: str  # Biggest Scoring Run
    lc: int  # Lead Changes
    tt: int  # Times Tied

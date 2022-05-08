from dataclasses import dataclass


@dataclass(frozen=True)
class CollectPlayByPlayInputdata:
    """スクレイピンから取得したPlay-by-play情報
    """
    schedule_key: int
    data_no: int # 何行目のテキストかを示す
    action_cd: str # どういったアクションなのかを判別するコード
    home_away: str  # ホームアウェイ区分(H, A, -) ※data_classから判別,official time outのときは'-'
    quoter: str # 何ピリオドかを示す
    time_remaining: str # 残り時間
    flg_point: bool # ポイントを取ったテキストの場合はTrue
    point_home: int # flg_pointがTrueのときのhomeの点数、FalseのときはNone
    point_away: int # flg_pointがTrueのときのawayの点数、FalseのときはNone
    player_id: str # プレイヤーID(ある場合)
    details: str # テキスト詳細

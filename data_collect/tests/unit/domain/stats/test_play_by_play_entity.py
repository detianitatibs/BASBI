from turtle import home
import pytest
from datetime import time

from src.domain.stats.play_by_play_entity import PlayByPlayEntity


class TestPlayByPlayEntity:
    @pytest.mark.parametrize(
        "schedule_key, data_no, action_cd,"\
        "home_away, quoter, time_remaining,"\
        "flg_point, point_home, point_away, details", [
            (
                1, 495, '81',
                'H', '1', time(0,5,40),
                True, 68, 54, '#33 トロイ フリースロー○(12点)'
            )
    ])
    def test_game_report_eintity_01(
        self, schedule_key, data_no, action_cd,
        home_away, quoter, time_remaining,
        flg_point, point_home, point_away, details):
        # CASE: パラメータを準備して
        # WHEN: エンティティを取得すると
        play_by_play = PlayByPlayEntity(
            schedule_key=schedule_key,
            data_no=data_no,
            action_cd=action_cd,
            home_away=home_away,
            quoter=quoter,
            time_remaining=time_remaining,
            flg_point=flg_point,
            point_home=point_home,
            point_away=point_away,
            details=details
        )

        # THEN: 正常に取得できる
        assert isinstance(play_by_play, PlayByPlayEntity)

        assert isinstance(play_by_play.schedule_key, int)
        assert play_by_play.schedule_key == schedule_key

        assert isinstance(play_by_play.data_no, int)
        assert play_by_play.data_no == data_no

        assert isinstance(play_by_play.action_cd, str)
        assert play_by_play.action_cd == action_cd

        assert isinstance(play_by_play.home_away, str)
        assert play_by_play.home_away == home_away

        assert isinstance(play_by_play.quoter, str)
        assert play_by_play.quoter == quoter

        assert isinstance(time_remaining, time)
        assert play_by_play.time_remaining == time_remaining

        assert isinstance(play_by_play.flg_point, bool)
        assert play_by_play.flg_point is flg_point

        assert isinstance(play_by_play.point_home, int)
        assert play_by_play.point_home == point_home

        assert isinstance(play_by_play.point_away, int)
        assert play_by_play.point_away == point_away

        assert isinstance(play_by_play.details, str)
        assert play_by_play.details == details

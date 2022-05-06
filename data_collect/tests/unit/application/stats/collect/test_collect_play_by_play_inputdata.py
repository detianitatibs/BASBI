import pytest

from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata


class TestCollectPlayByPlayInputdata:
    @pytest.mark.parametrize(
        "schedule_key, data_no, action_cd,"\
        "home_away, quoter, time_remaining,"\
        "flg_point, point_home, point_away,"\
        "player_id, details", [
            (
                1, 2, '86',
                'H', '1', '10:00',
                False, None, None, 
                '9032', '#13 菊地 プレイヤーイン'
            )
        ]
    )
    def test_collect_play_by_play_inputdata_01(
        self, schedule_key, data_no, action_cd,
        home_away, quoter, time_remaining,
        flg_point, point_home, point_away,
        player_id, details
    ):
        # CASE: パラメータを準備して
        # WHEN: インプットデータを取得すると
        collect_play_by_play_inputdata = CollectPlayByPlayInputdata(
            schedule_key=schedule_key,
            data_no=data_no,
            action_cd=action_cd,
            home_away=home_away,
            quoter=quoter,
            time_remaining=time_remaining,
            flg_point=flg_point,
            point_home=point_home,
            point_away=point_away,
            player_id=player_id,
            details=details
        )

        # THEN: 正常に取得できる
        assert isinstance(
            collect_play_by_play_inputdata,
            CollectPlayByPlayInputdata
        )

        assert isinstance(collect_play_by_play_inputdata.schedule_key, int)
        assert collect_play_by_play_inputdata.schedule_key == schedule_key

        assert isinstance(collect_play_by_play_inputdata.data_no, int)
        assert collect_play_by_play_inputdata.data_no == data_no

        assert isinstance(collect_play_by_play_inputdata.action_cd, str)
        assert collect_play_by_play_inputdata.action_cd == action_cd

        assert isinstance(collect_play_by_play_inputdata.home_away, str)
        assert collect_play_by_play_inputdata.home_away == home_away

        assert isinstance(collect_play_by_play_inputdata.quoter, str)
        assert collect_play_by_play_inputdata.quoter == quoter

        assert isinstance(collect_play_by_play_inputdata.time_remaining, str)
        assert collect_play_by_play_inputdata.time_remaining == time_remaining

        assert isinstance(collect_play_by_play_inputdata.flg_point, bool)
        assert collect_play_by_play_inputdata.flg_point == flg_point

        assert isinstance(collect_play_by_play_inputdata.point_home, int) or collect_play_by_play_inputdata.point_home is None
        assert collect_play_by_play_inputdata.point_home == point_home

        assert isinstance(collect_play_by_play_inputdata.point_away, int) or collect_play_by_play_inputdata.point_away is None
        assert collect_play_by_play_inputdata.point_away == point_away

        assert isinstance(collect_play_by_play_inputdata.player_id, str) or collect_play_by_play_inputdata.player_id is None
        assert collect_play_by_play_inputdata.player_id == player_id

        assert isinstance(collect_play_by_play_inputdata.details, str)
        assert collect_play_by_play_inputdata.details == details

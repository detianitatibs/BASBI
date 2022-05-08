from typing import List

import pytest

from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata


class TestCollectGameInfoInputdata:
    @pytest.mark.parametrize(
        "schedule_key, title, tipoff, sec,"\
        "arena, attendance, referee,"\
        "home_fullname, home_name, away_fullname, away_name,"\
        "home_score, home_score_q, away_score, away_score_q",[
            (
                1, '2016-17 B1リーグ 2016/09/22 A東京 VS 琉球 - B.LEAGUE（Bリーグ）公式サイト', '18:55 TIP OFF', '第1節',
                '会場：国立代々木競技場第一体育館', '人数：9132人', 'レフェリー：宇田川\u3000貴生／片寄\u3000達／平原\u3000勇次',
                'アルバルク東京', 'A東京', '琉球ゴールデンキングス', '琉球',
                80, [26, 17, 21, 16], 75, [19, 17, 15, 24]
            )
        ]
    )
    def test_collect_game_info_inputdata_01(
        self, schedule_key, title, tipoff, sec,
        arena, attendance, referee,
        home_fullname, home_name, away_fullname, away_name, 
        home_score, home_score_q,
        away_score, away_score_q
    ):
        # CASE: パラメータを準備して
        # WHEN: インプットデータを取得すると
        collect_game_info_inputdata = CollectGameInfoInputdata(
            schedule_key=schedule_key,
            title=title,
            tipoff=tipoff,
            sec=sec,
            arena=arena,
            attendance=attendance,
            referee=referee,
            home_fullname=home_fullname,
            home_name=home_name,
            away_fullname=away_fullname,
            away_name=away_name,
            home_score=home_score,
            home_score_q=home_score_q,
            away_score=away_score,
            away_score_q=away_score_q
        )

        # THEN: 正常に取得できる
        assert isinstance(
            collect_game_info_inputdata,
            CollectGameInfoInputdata
        )

        assert isinstance(collect_game_info_inputdata.schedule_key, int)
        assert collect_game_info_inputdata.schedule_key == schedule_key

        assert isinstance(collect_game_info_inputdata.title, str)
        assert collect_game_info_inputdata.title == title

        assert isinstance(collect_game_info_inputdata.tipoff, str)
        assert collect_game_info_inputdata.tipoff == tipoff

        assert isinstance(collect_game_info_inputdata.sec, str)
        assert collect_game_info_inputdata.sec == sec

        assert isinstance(collect_game_info_inputdata.arena, str)
        assert collect_game_info_inputdata.arena == arena

        assert isinstance(collect_game_info_inputdata.attendance, str)
        assert collect_game_info_inputdata.attendance == attendance

        assert isinstance(collect_game_info_inputdata.referee, str)
        assert collect_game_info_inputdata.referee == referee

        assert isinstance(collect_game_info_inputdata.home_fullname, str)
        assert collect_game_info_inputdata.home_fullname == home_fullname

        assert isinstance(collect_game_info_inputdata.home_name, str)
        assert collect_game_info_inputdata.home_name == home_name

        assert isinstance(collect_game_info_inputdata.away_fullname, str)
        assert collect_game_info_inputdata.away_fullname == away_fullname

        assert isinstance(collect_game_info_inputdata.away_name, str)
        assert collect_game_info_inputdata.away_name == away_name

        assert isinstance(collect_game_info_inputdata.home_score, int)
        assert collect_game_info_inputdata.home_score == home_score

        assert isinstance(collect_game_info_inputdata.home_score_q, List)
        assert len(collect_game_info_inputdata.home_score_q) > 0

        assert isinstance(collect_game_info_inputdata.away_score, int)
        assert collect_game_info_inputdata.away_score == away_score

        assert isinstance(collect_game_info_inputdata.away_score_q, List)
        assert len(collect_game_info_inputdata.away_score_q) > 0

import pytest
from datetime import date, time

from src.domain.stats.game_info_entity import GameInfoEntity


class TestGameInfoEntity:
    @pytest.mark.parametrize(
        "schedule_key, game_date, tipoff, season,"\
        "division, sec, arena, referee_1, referee_2, referee_3,"\
        "home_fullname, home_name, home_score,"\
        "home_score_q,"\
        "away_fullname, away_name, away_score,"\
        "away_score_q,", [
            (
                1, date(2021, 10, 1), time(13, 0, 0), '2021-22',
                'B1', 1, '武道館', '審判1', '審判2', '審判3',
                '東京アパッチ', 'アパッチ', 86,
                [24, 21, 23, 32],
                '和歌山トライアンズ', 'トライアンズ', 85,
                [10, 32, 23, 32]
            ),
            (
                2, date(2021, 10, 1), time(13, 0, 0), '2021-22',
                'B1', 1, '武道館', '審判1', '審判2', '審判3',
                '東京アパッチ', 'アパッチ', 86,
                [24, 21, 23, 32, 5, 10],
                '和歌山トライアンズ', 'トライアンズ', 85,
                [10, 32, 23, 32, 5, 8]
            )
    ])
    def test_game_info_entity_01(
        self, schedule_key, game_date, tipoff, season,
        division, sec, arena, referee_1, referee_2, referee_3,
        home_fullname, home_name, home_score,
        home_score_q,
        away_fullname, away_name, away_score,
        away_score_q
    ):
        # CASE: パラメータを準備して
        # WHEN: エンティティを取得すると
        game_info = GameInfoEntity(
            schedule_key=schedule_key,
            game_date=game_date,
            tipoff=tipoff,
            season=season,
            division=division,
            sec=sec,
            arena=arena,
            referee_1=referee_1,
            referee_2=referee_2,
            referee_3=referee_3,
            home_fullname=home_fullname,
            home_name=home_name,
            home_score=home_score,
            home_score_q=home_score_q,
            away_fullname=away_fullname,
            away_name=away_name,
            away_score=away_score,
            away_score_q=away_score_q
        )

        # THEN: 正常に取得できる
        isinstance(game_info, GameInfoEntity)
        
        isinstance(game_info.schedule_key, int)
        assert game_info.schedule_key == schedule_key

        isinstance(game_info.game_date, date)
        assert game_info.game_date == game_date
        
        isinstance(game_info.tipoff, time)
        assert game_info.tipoff == tipoff

        isinstance(game_info.season, str)
        assert game_info.season == season

        isinstance(game_info.division, str)
        assert game_info.division == division

        isinstance(game_info.sec, int)
        assert game_info.sec == sec

        isinstance(game_info.arena, str)
        assert game_info.arena == arena

        isinstance(game_info.referee_1, str)
        assert game_info.referee_1 == referee_1

        isinstance(game_info.referee_2, str)
        assert game_info.referee_2 == referee_2

        isinstance(game_info.referee_3, str)
        assert game_info.referee_3 == referee_3

        isinstance(game_info.home_fullname, str)
        assert game_info.home_fullname == home_fullname

        isinstance(game_info.home_name, str)
        assert game_info.home_name == home_name

        isinstance(game_info.home_score, int)
        assert game_info.home_score == home_score

        isinstance(game_info.home_score_q, list)
        assert game_info.home_score_q == home_score_q

        isinstance(game_info.away_fullname, str)
        assert game_info.away_fullname == away_fullname

        isinstance(game_info.away_name, str)
        assert game_info.away_name == away_name

        isinstance(game_info.away_score, int)
        assert game_info.away_score == away_score

        isinstance(game_info.away_score_q, list)
        assert game_info.away_score_q == away_score_q

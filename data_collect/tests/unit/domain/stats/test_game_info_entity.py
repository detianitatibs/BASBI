import pytest
from datetime import date, time

from src.domain.stats.game_info_entity import GameInfoEntity


class TestGameInfoEntity:
    @pytest.mark.parametrize(
        "schedule_key, title, game_date, tipoff, season,"\
        "division, sec, arena, attendance, referee_1, referee_2, referee_3,"\
        "home_fullname, home_name, home_score,"\
        "home_score_q,"\
        "away_fullname, away_name, away_score,"\
        "away_score_q,", [
            (
                1, '20YY-YY BXリーグ YYYY/mm/dd Home VS Away - B.LEAGUE（Bリーグ）公式サイト', 
                date(2021, 10, 1), time(13, 0, 0), '2021-22',
                'B1', 1, '武道館', 1000, '審判1', '審判2', '審判3',
                '東京アパッチ', 'アパッチ', 86,
                [24, 21, 23, 32],
                '和歌山トライアンズ', 'トライアンズ', 85,
                [10, 32, 23, 32]
            ),
            (
                2, '20YY-YY BXリーグ YYYY/mm/dd Home VS Away - B.LEAGUE（Bリーグ）公式サイト', 
                date(2021, 10, 1), time(13, 0, 0), '2021-22',
                'B1', 1, '武道館', 1000, '審判1', '審判2', '審判3',
                '東京アパッチ', 'アパッチ', 86,
                [24, 21, 23, 32, 5, 10],
                '和歌山トライアンズ', 'トライアンズ', 85,
                [10, 32, 23, 32, 5, 8]
            )
    ])
    def test_game_info_entity_01(
        self, schedule_key, title, game_date, tipoff, season,
        division, sec, arena, attendance, referee_1, referee_2, referee_3,
        home_fullname, home_name, home_score,
        home_score_q,
        away_fullname, away_name, away_score,
        away_score_q
    ):
        # CASE: パラメータを準備して
        # WHEN: エンティティを取得すると
        game_info = GameInfoEntity(
            schedule_key=schedule_key,
            title=title,
            game_date=game_date,
            tipoff=tipoff,
            season=season,
            division=division,
            sec=sec,
            arena=arena,
            attendance=attendance,
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
        assert isinstance(game_info, GameInfoEntity)
        
        assert isinstance(game_info.schedule_key, int)
        assert game_info.schedule_key == schedule_key

        assert isinstance(game_info.title, str)
        assert game_info.title == title

        assert isinstance(game_info.game_date, date)
        assert game_info.game_date == game_date
        
        assert isinstance(game_info.tipoff, time)
        assert game_info.tipoff == tipoff

        assert isinstance(game_info.season, str)
        assert game_info.season == season

        assert isinstance(game_info.division, str)
        assert game_info.division == division

        assert isinstance(game_info.sec, int)
        assert game_info.sec == sec

        assert isinstance(game_info.arena, str)
        assert game_info.arena == arena

        assert isinstance(game_info.attendance, int)
        assert game_info.attendance == attendance

        assert isinstance(game_info.referee_1, str)
        assert game_info.referee_1 == referee_1

        assert isinstance(game_info.referee_2, str)
        assert game_info.referee_2 == referee_2

        assert isinstance(game_info.referee_3, str)
        assert game_info.referee_3 == referee_3

        assert isinstance(game_info.home_fullname, str)
        assert game_info.home_fullname == home_fullname

        assert isinstance(game_info.home_name, str)
        assert game_info.home_name == home_name

        assert isinstance(game_info.home_score, int)
        assert game_info.home_score == home_score

        assert isinstance(game_info.home_score_q, list)
        assert game_info.home_score_q == home_score_q

        assert isinstance(game_info.away_fullname, str)
        assert game_info.away_fullname == away_fullname

        assert isinstance(game_info.away_name, str)
        assert game_info.away_name == away_name

        assert isinstance(game_info.away_score, int)
        assert game_info.away_score == away_score

        assert isinstance(game_info.away_score_q, list)
        assert game_info.away_score_q == away_score_q

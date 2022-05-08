from typing import List

import pytest
from injector import Injector, Module, Binder

from src.domain.stats.game_info_entity import GameInfoEntity
from src.domain.stats.game_report_entity import GamerReportEntity
from src.domain.stats.box_score_entity import BoxScoreEntity
from src.domain.stats.play_by_play_entity import PlayByPlayEntity
from src.domain.stats.i_game_info_repository import IGameInfoRepository
from src.domain.stats.i_game_report_repository import IGameReportRepository
from src.domain.stats.i_box_score_repository import IBoxScoreRepository
from src.domain.stats.i_play_by_play_repository import IPlayByPlayRepository
from src.application.stats.collect.collect_stats_interactor import CollectStatsInteractor
from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata
from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata
from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata
from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata


class DummyGameInfoRepository(IGameInfoRepository):
    def save(self):
        pass

class DummyGameReportRepository(IGameReportRepository):
    def save(self):
        pass

class DummyBoxScoreRepository(IBoxScoreRepository):
    def save(self):
        pass

class DummyPlayByPlayRepository(IPlayByPlayRepository):
    def save(self):
        pass

class TaskDIModule(Module):
    # テスト用にダミークラスをinjectする
    def configure(self, binder: Binder) -> None:
        binder.bind(IGameInfoRepository, to=DummyGameInfoRepository)
        binder.bind(IGameReportRepository, to=DummyGameReportRepository)
        binder.bind(IBoxScoreRepository, to=DummyBoxScoreRepository)
        binder.bind(IPlayByPlayRepository, to=DummyPlayByPlayRepository)

class TestCollectStatsInteractor():
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
    def test_translate_game_info_01(
        self, schedule_key, title, tipoff, sec,
        arena, attendance, referee,
        home_fullname, home_name, away_fullname, away_name, 
        home_score, home_score_q,
        away_score, away_score_q
    ):
        # CASE: inputdataを用意して
        inputdata = CollectGameInfoInputdata(
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

        # WHEN: 変換を実施すると
        injector = Injector([TaskDIModule()])
        csi = injector.get(CollectStatsInteractor)
        entity = csi._translate_game_info(inputdata)

        # THEN: 変換されたEntityが取得できる
        assert isinstance(entity, GameInfoEntity)
    
    @pytest.mark.parametrize(
        "schedule_key, home_away, team_name,"\
        "fgm, fga, fgr, fgm3, fga3, fgr3,"\
        "ftm, fta, ftr, ofr, der, tor,"\
        "ast, to, st, bo, fo, fbp, bl,"\
        "pp, pto, scp, bsr, lc, tt",[
            (
                1, 'H', 'A東京',
                24, 50, '48%', 9, 25, '36%',
                5, 12, '41.7%', 15, 29, 44,
                17, 15, 10, 5, 16, 6, 15,
                38, 14, 10, '7-0\n(9-2)', 0, 1
            )
        ]
    )
    def test_translate_game_report_01(
        self, schedule_key, home_away, team_name,
        fgm, fga, fgr, fgm3, fga3, fgr3,
        ftm, fta, ftr, ofr, der, tor,
        ast, to, st, bo, fo, fbp, bl,
        pp, pto, scp, bsr, lc, tt
    ):
        # CASE: inputdataを用意して
        inputdata = CollectGameReportInputdata(
            schedule_key=schedule_key,
            home_away=home_away,
            team_name=team_name,
            fgm=fgm,
            fga=fga,
            fgr=fgr,
            fgm3=fgm3,
            fga3=fga3,
            fgr3=fgr3,
            ftm=ftm,
            fta=fta,
            ftr=ftr,
            ofr=ofr,
            der=der,
            tor=tor,
            ast=ast,
            to=to,
            st=st,
            bo=bo,
            fo=fo,
            fbp=fbp,
            bl=bl,
            pp=pp,
            pto=pto,
            scp=scp,
            bsr=bsr,
            lc=lc,
            tt=tt
        )
        list_inputdata = [inputdata]

        # WHEN: 変換を実施すると
        injector = Injector([TaskDIModule()])
        csi = injector.get(CollectStatsInteractor)
        list_entity = csi._translate_game_report(list_inputdata)

        # THEN: 変換されたEntityが取得できる
        assert isinstance(list_entity, List)
        assert isinstance(list_entity[0], GamerReportEntity)
    
    @pytest.mark.parametrize(
        "schedule_key, home_away, team_name,"\
        "quoter, player_id, no, start_flg,"\
        "player_name, position, minutes,"\
        "pts, fgm, fga, fgr, fgm3, fga3, fgr3,"\
        "ftm, fta, ftr, ofr, der, tor, ast,"\
        "to, st, bo, bsr, fo, fd, dunk, eff", [
            (
                1, 'A', '琉球ゴールデンキングス',
                '4', '9384', '34', '〇',
                'ラモント・ハミルトン', 'PF/C', '05:18',
                2, 1, 1, '100.0%', 0, 0, '95.7%',
                0, 0, '-', 1, 3, 4, 1,
                2, 1, 0, 0, 0, 0, 0, 6.0
            ),
            (
                1,  'A', '琉球ゴールデンキングス',
                '4', '9417', None, '',
                'TEAM / COACHES', '', '',
                0, 0, 0, '-', 0, 0, '-',
                0, 0, '-', 1, 0, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 1.0
            ),
            (
                1,  'A', '琉球ゴールデンキングス',
                '4', None, None, '',
                '合計', '', '50:00',
                0, 0, 0, '-', 0, 0, '-',
                0, 0, '-', 1, 0, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 1.0
            )
        ]
    )
    def test_translate_box_score_01(
        self, schedule_key, home_away, team_name,
        quoter, player_id, no, start_flg,
        player_name, position, minutes,
        pts, fgm, fga, fgr, fgm3, fga3, fgr3,
        ftm, fta, ftr, ofr, der, tor, ast,
        to, st, bo, bsr, fo, fd, dunk, eff
    ):
        # CASE: inputdataを用意して
        inputdata = CollectBoxScoreInputdata(
            schedule_key=schedule_key,
            home_away=home_away,
            team_name=team_name,
            quoter=quoter,
            player_id=player_id,
            no=no,
            start_flg=start_flg,
            player_name=player_name,
            position=position,
            minutes=minutes,
            pts=pts,
            fgm=fgm,
            fga=fga,
            fgr=fgr,
            fgm3=fgm3,
            fga3=fga3,
            fgr3=fgr3,
            ftm=ftm,
            fta=fta,
            ftr=ftr,
            ofr=ofr,
            der=der,
            tor=tor,
            ast=ast,
            to=to,
            st=st,
            bo=bo,
            bsr=bsr,
            fo=fo,
            fd=fd,
            dunk=dunk,
            eff=eff
        )
        list_inputdata = [inputdata]

        # WHEN: 変換を実施すると
        injector = Injector([TaskDIModule()])
        csi = injector.get(CollectStatsInteractor)
        list_entity = csi._translate_box_score(list_inputdata)

        # THEN: 変換されたEntityが取得できる
        assert isinstance(list_entity, List)
        assert isinstance(list_entity[0], BoxScoreEntity)

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
    def test_translate_play_by_play_01(
        self, schedule_key, data_no, action_cd,
        home_away, quoter, time_remaining,
        flg_point, point_home, point_away,
        player_id, details
    ):
        # CASE: inputdataを用意して
        inputdata = CollectPlayByPlayInputdata(
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
        list_inputdata = [inputdata]

        # WHEN: 変換を実施すると
        injector = Injector([TaskDIModule()])
        csi = injector.get(CollectStatsInteractor)
        list_entity = csi._translate_play_by_play(list_inputdata)

        # THEN: 変換されたEntityが取得できる
        assert isinstance(list_entity, List)
        assert isinstance(list_entity[0], PlayByPlayEntity)

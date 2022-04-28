from re import A
from turtle import home
import pytest

from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata


class TestCollectGameReportInputdata:
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
    def test_collect_game_report_inputdata_01(
        self, schedule_key, home_away, team_name,
        fgm, fga, fgr, fgm3, fga3, fgr3,
        ftm, fta, ftr, ofr, der, tor,
        ast, to, st, bo, fo, fbp, bl,
        pp, pto, scp, bsr, lc, tt
    ):
        # CASE: パラメータを準備して
        # WHEN: インプットデータを取得すると
        collect_game_report_inputdata = CollectGameReportInputdata(
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

        # THEN: 正常に取得できる
        assert isinstance(
            collect_game_report_inputdata,
            CollectGameReportInputdata
        )

        assert isinstance(collect_game_report_inputdata.schedule_key, int)
        assert collect_game_report_inputdata.schedule_key == schedule_key

        assert isinstance(collect_game_report_inputdata.home_away, str)
        assert collect_game_report_inputdata.home_away == home_away

        assert isinstance(collect_game_report_inputdata.team_name, str)
        assert collect_game_report_inputdata.team_name == team_name

        assert isinstance(collect_game_report_inputdata.fgm, int)
        assert collect_game_report_inputdata.fgm == fgm

        assert isinstance(collect_game_report_inputdata.fga, int)
        assert collect_game_report_inputdata.fga == fga

        assert isinstance(collect_game_report_inputdata.fgr, str)
        assert collect_game_report_inputdata.fgr == fgr

        assert isinstance(collect_game_report_inputdata.fgm3, int)
        assert collect_game_report_inputdata.fgm3 == fgm3

        assert isinstance(collect_game_report_inputdata.fga3, int)
        assert collect_game_report_inputdata.fga3 == fga3

        assert isinstance(collect_game_report_inputdata.fgr3, str)
        assert collect_game_report_inputdata.fgr3 == fgr3

        assert isinstance(collect_game_report_inputdata.ftm, int)
        assert collect_game_report_inputdata.ftm == ftm

        assert isinstance(collect_game_report_inputdata.fta, int)
        assert collect_game_report_inputdata.fta == fta

        assert isinstance(collect_game_report_inputdata.ftr, str)
        assert collect_game_report_inputdata.ftr == ftr

        assert isinstance(collect_game_report_inputdata.ofr, int)
        assert collect_game_report_inputdata.ofr == ofr

        assert isinstance(collect_game_report_inputdata.der, int)
        assert collect_game_report_inputdata.der == der

        assert isinstance(collect_game_report_inputdata.tor, int)
        assert collect_game_report_inputdata.tor == tor

        assert isinstance(collect_game_report_inputdata.ast, int)
        assert collect_game_report_inputdata.ast == ast

        assert isinstance(collect_game_report_inputdata.to, int)
        assert collect_game_report_inputdata.to == to

        assert isinstance(collect_game_report_inputdata.st, int)
        assert collect_game_report_inputdata.st == st

        assert isinstance(collect_game_report_inputdata.bo, int)
        assert collect_game_report_inputdata.bo == bo

        assert isinstance(collect_game_report_inputdata.fo, int)
        assert collect_game_report_inputdata.fo == fo
        
        assert isinstance(collect_game_report_inputdata.fbp, int)
        assert collect_game_report_inputdata.fbp == fbp

        assert isinstance(collect_game_report_inputdata.bl, int)
        assert collect_game_report_inputdata.bl == bl

        assert isinstance(collect_game_report_inputdata.pp, int)
        assert collect_game_report_inputdata.pp == pp

        assert isinstance(collect_game_report_inputdata.pto, int)
        assert collect_game_report_inputdata.pto == pto

        assert isinstance(collect_game_report_inputdata.scp, int)
        assert collect_game_report_inputdata.scp == scp

        assert isinstance(collect_game_report_inputdata.bsr, str)
        assert collect_game_report_inputdata.bsr == bsr

        assert isinstance(collect_game_report_inputdata.lc, int)
        assert collect_game_report_inputdata.lc == lc

        assert isinstance(collect_game_report_inputdata.tt, int)
        assert collect_game_report_inputdata.tt == tt

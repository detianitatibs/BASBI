import pytest

from src.domain.stats.game_report_entity import GamerReportEntity


class TestGameReportEntity:
    @pytest.mark.parametrize(
        "schedule_key, home_away, team_name,"\
        "fgm, fga, fgr, fgm3, fga3, fgr3, ftm, fta, ftr,"\
        "ofr, der, tor, ast, to, st, bo, fo,"\
        "fbp, bl, pp, pto, scp, bsr, lc, tt", [
            (
                1, 'h', '琉球',
                10, 20, 50.0, 3, 10, 3.33, 10, 20, 5.3,
                10, 4, 10, 30, 30, 20, 10, 3,
                2, 3, 4, 2, 3, '9-0(34-39)', 20, 1
            )
    ])
    def test_game_report_eintity_01(
        self, schedule_key, home_away, team_name,
        fgm, fga, fgr, fgm3, fga3, fgr3, ftm, fta, ftr,
        ofr, der, tor, ast, to, st, bo, fo,
        fbp, bl, pp, pto, scp, bsr, lc, tt):
        # CASE: パラメータを準備して
        # WHEN: エンティティを取得すると
        game_report = GamerReportEntity(
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
        assert isinstance(game_report, GamerReportEntity)

        assert isinstance(game_report.schedule_key, int)
        assert game_report.schedule_key == schedule_key

        assert isinstance(game_report.home_away, str)
        assert game_report.home_away == home_away

        assert isinstance(game_report.team_name, str)
        assert game_report.team_name == team_name

        assert isinstance(game_report.fgm, int)
        assert game_report.fgm == fgm

        assert isinstance(game_report.fga, int)
        assert game_report.fga == fga

        assert isinstance(game_report.fgr, float)
        assert game_report.fgr == fgr

        assert isinstance(game_report.fgm3, int)
        assert game_report.fgm3 == fgm3

        assert isinstance(game_report.fga3, int)
        assert game_report.fga3 == fga3

        assert isinstance(game_report.fgr3, float)
        assert game_report.fgr3 == fgr3

        assert isinstance(game_report.ftm, int)
        assert game_report.ftm == ftm

        assert isinstance(game_report.fta, int)
        assert game_report.fta == fta

        assert isinstance(game_report.ftr, float)
        assert game_report.ftr == ftr

        assert isinstance(game_report.ofr, int)
        assert game_report.ofr == ofr

        assert isinstance(game_report.der, int)
        assert game_report.der == der

        assert isinstance(game_report.tor, int)
        assert game_report.tor == tor

        assert isinstance(game_report.ast, int)
        assert game_report.ast == ast

        assert isinstance(game_report.to, int)
        assert game_report.to == to

        assert isinstance(game_report.st, int)
        assert game_report.st == st

        assert isinstance(game_report.bo, int)
        assert game_report.bo == bo

        assert isinstance(game_report.fo, int)
        assert game_report.fo == fo

        assert isinstance(game_report.fbp, int)
        assert game_report.fbp == fbp

        assert isinstance(game_report.bl, int)
        assert game_report.bl == bl

        assert isinstance(game_report.pp, int)
        assert game_report.pp == pp

        assert isinstance(game_report.pto, int)
        assert game_report.pto == pto

        assert isinstance(game_report.scp, int)
        assert game_report.scp == scp

        assert isinstance(game_report.bsr, str)
        assert game_report.bsr == bsr

        assert isinstance(game_report.lc, int)
        assert game_report.lc == lc

        assert isinstance(game_report.tt, int)
        assert game_report.tt == tt

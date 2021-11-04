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
                10, 20, 50, 3, 10, 3.33, 10, 20, 5.3,
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
        isinstance(game_report, GamerReportEntity)

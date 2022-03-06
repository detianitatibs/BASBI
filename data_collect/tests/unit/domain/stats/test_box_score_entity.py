import pytest
from datetime import time

from src.domain.stats.box_score_entity import BoxScoreEntithy


class TestBoxScoreEntity:
    @pytest.mark.parametrize(
        "schedule_key, home_away,"\
        "team_name, no, player_id, player_name,"\
        "quoter, start_flg, position, minutes,"\
        "pts, fgm, fga, fgr,"\
        "fgm3, fga3, fgr3, ftm, fta, ftr,"\
        "ofr, der, tor, ast, to, st, bo, bsr,"\
        "fo, fd, dunk, eff", [
        (
            141, 'H',
            "横浜ビー・コルセアーズ", 0, 8712, "細谷 将司",
            "ALL", True, "PG", time(0, 36, 11),
            10, 4, 9, 44.4,
            1, 4, 25.0, 1, 2, 50.0,
            0, 3, 3, 1, 4, 0, 0, 2,
            0, 2, 0, 4
        )
    ])
    def test_box_score_entity_01(
        self, schedule_key, home_away,
        team_name, no, player_id, player_name,
        quoter, start_flg, position, minutes,
        pts, fgm, fga, fgr,
        fgm3, fga3, fgr3, ftm, fta, ftr,
        ofr, der, tor, ast, to, st, bo, bsr,
        fo, fd, dunk, eff
    ):
        # CASE: パラメータを準備して
        # WHEN: エンティティを取得すると
        box_score = BoxScoreEntithy(
            schedule_key=schedule_key,
            home_away=home_away,
            team_name=team_name,
            no=no,
            player_id=player_id,
            player_name=player_name,
            quoter=quoter,
            start_flg=start_flg,
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
        # THEN: 正常に取得できる
        isinstance(box_score, BoxScoreEntithy)

        isinstance(box_score.schedule_key, int)
        assert box_score.schedule_key == schedule_key

        isinstance(box_score.home_away, str)
        assert box_score.home_away == home_away

        isinstance(box_score.team_name, str)
        assert box_score.team_name == team_name

        isinstance(box_score.no, int)
        assert box_score.no == no

        isinstance(box_score.player_id, int)
        assert box_score.player_id == player_id

        isinstance(box_score.player_name, int)
        assert box_score.player_name == player_name

        isinstance(box_score.quoter, str)
        assert box_score.quoter == quoter

        isinstance(box_score.start_flg, bool)
        assert box_score.start_flg == start_flg

        isinstance(box_score.position, str)
        assert box_score.position == position

        isinstance(box_score.minutes, time)
        assert box_score.minutes == minutes

        isinstance(box_score.pts, int)
        assert box_score.pts == pts

        isinstance(box_score.fgm, int)
        assert box_score.fgm == fgm

        isinstance(box_score.fga, int)
        assert box_score.fga == fga

        isinstance(box_score.fgr, float)
        assert box_score.fgr == fgr

        isinstance(box_score.fgm3, int)
        assert box_score.fgm3 == fgm3

        isinstance(box_score.fga3, int)
        assert box_score.fga3 == fga3
        
        isinstance(box_score.fgr3, float)
        assert box_score.fgr3 == fgr3

        isinstance(box_score.ftm, int)
        assert box_score.ftm == ftm

        isinstance(box_score.fta, int)
        assert box_score.fta == fta

        isinstance(box_score.ftr, float)
        assert box_score.ftr == ftr

        isinstance(box_score.ofr, int)
        assert box_score.ofr == ofr

        isinstance(box_score.der, int)
        assert box_score.der == der

        isinstance(box_score.tor, int)
        assert box_score.tor == tor

        isinstance(box_score.ast, int)
        assert box_score.ast == ast

        isinstance(box_score.to, int)
        assert box_score.to == to

        isinstance(box_score.st, int)
        assert box_score.st == st

        isinstance(box_score.bo, int)
        assert box_score.bo == bo

        isinstance(box_score.bsr, int)
        assert box_score.bsr == bsr

        isinstance(box_score.fo, int)
        assert box_score.fo == fo

        isinstance(box_score.fd, int)
        assert box_score.fd == fd

        isinstance(box_score.dunk, int)
        assert box_score.dunk == dunk

        isinstance(box_score.eff, float)
        assert box_score.eff == eff

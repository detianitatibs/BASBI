import pytest
from datetime import time

from src.domain.stats.box_score_entity import BoxScoreEntity


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
            "ALL", True, "PG", '36:11',
            10, 4, 9, 44.4,
            1, 4, 25.0, 1, 2, 50.0,
            0, 3, 3, 1, 4, 0, 0, 2,
            0, 2, 0, 4.0
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
        box_score = BoxScoreEntity(
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
        assert isinstance(box_score, BoxScoreEntity)

        assert isinstance(box_score.schedule_key, int)
        assert box_score.schedule_key == schedule_key

        assert isinstance(box_score.home_away, str)
        assert box_score.home_away == home_away

        assert isinstance(box_score.team_name, str)
        assert box_score.team_name == team_name

        assert isinstance(box_score.no, int)
        assert box_score.no == no

        assert isinstance(box_score.player_id, int)
        assert box_score.player_id == player_id

        assert isinstance(box_score.player_name, str)
        assert box_score.player_name == player_name

        assert isinstance(box_score.quoter, str)
        assert box_score.quoter == quoter

        assert isinstance(box_score.start_flg, bool)
        assert box_score.start_flg == start_flg

        assert isinstance(box_score.position, str)
        assert box_score.position == position

        assert isinstance(box_score.minutes, str)
        assert box_score.minutes == minutes

        assert isinstance(box_score.pts, int)
        assert box_score.pts == pts

        assert isinstance(box_score.fgm, int)
        assert box_score.fgm == fgm

        assert isinstance(box_score.fga, int)
        assert box_score.fga == fga

        assert isinstance(box_score.fgr, float)
        assert box_score.fgr == fgr

        assert isinstance(box_score.fgm3, int)
        assert box_score.fgm3 == fgm3

        assert isinstance(box_score.fga3, int)
        assert box_score.fga3 == fga3
        
        assert isinstance(box_score.fgr3, float)
        assert box_score.fgr3 == fgr3

        assert isinstance(box_score.ftm, int)
        assert box_score.ftm == ftm

        assert isinstance(box_score.fta, int)
        assert box_score.fta == fta

        assert isinstance(box_score.ftr, float)
        assert box_score.ftr == ftr

        assert isinstance(box_score.ofr, int)
        assert box_score.ofr == ofr

        assert isinstance(box_score.der, int)
        assert box_score.der == der

        assert isinstance(box_score.tor, int)
        assert box_score.tor == tor

        assert isinstance(box_score.ast, int)
        assert box_score.ast == ast

        assert isinstance(box_score.to, int)
        assert box_score.to == to

        assert isinstance(box_score.st, int)
        assert box_score.st == st

        assert isinstance(box_score.bo, int)
        assert box_score.bo == bo

        assert isinstance(box_score.bsr, int)
        assert box_score.bsr == bsr

        assert isinstance(box_score.fo, int)
        assert box_score.fo == fo

        assert isinstance(box_score.fd, int)
        assert box_score.fd == fd

        assert isinstance(box_score.dunk, int)
        assert box_score.dunk == dunk

        assert isinstance(box_score.eff, float)
        assert box_score.eff == eff

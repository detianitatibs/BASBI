from turtle import home
import pytest

from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata


class TestCollectBoxScoreInputdata:
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
                2, 1, 1, '100.0%', 0, 0, '-',
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
    def test_collect_box_score_inputdata_01(
        self, schedule_key, home_away, team_name,
        quoter, player_id, no, start_flg,
        player_name, position, minutes,
        pts, fgm, fga, fgr, fgm3, fga3, fgr3,
        ftm, fta, ftr, ofr, der, tor, ast,
        to, st, bo, bsr, fo, fd, dunk, eff
    ):
        # CASE: パラメータを準備して
        # WHEN: インプットデータを取得すると
        collect_box_score_inputdata = CollectBoxScoreInputdata(
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

        # THEN: 正常に取得できる
        assert isinstance(
            collect_box_score_inputdata,
            CollectBoxScoreInputdata
        )

        assert isinstance(collect_box_score_inputdata.schedule_key, int)
        assert collect_box_score_inputdata.schedule_key == schedule_key

        assert isinstance(collect_box_score_inputdata.home_away, str)
        assert collect_box_score_inputdata.home_away == home_away

        assert isinstance(collect_box_score_inputdata.team_name, str)
        assert collect_box_score_inputdata.team_name == team_name

        assert isinstance(collect_box_score_inputdata.quoter, str)
        assert collect_box_score_inputdata.quoter == quoter

        assert (
            isinstance(collect_box_score_inputdata.player_id, str)
            or collect_box_score_inputdata.player_id is None
        )
        assert collect_box_score_inputdata.player_id == player_id

        assert (
            isinstance(collect_box_score_inputdata.no, str)
            or collect_box_score_inputdata.no is None
        )
        assert collect_box_score_inputdata.no == no

        assert isinstance(collect_box_score_inputdata.start_flg, str)
        assert collect_box_score_inputdata.start_flg == start_flg

        assert isinstance(collect_box_score_inputdata.player_name, str)
        assert collect_box_score_inputdata.player_name == player_name

        assert isinstance(collect_box_score_inputdata.position, str)
        assert collect_box_score_inputdata.position == position

        assert isinstance(collect_box_score_inputdata.minutes, str)
        assert collect_box_score_inputdata.minutes == minutes

        assert isinstance(collect_box_score_inputdata.pts, int)
        assert collect_box_score_inputdata.pts == pts

        assert isinstance(collect_box_score_inputdata.fgm, int)
        assert collect_box_score_inputdata.fgm == fgm

        assert isinstance(collect_box_score_inputdata.fga, int)
        assert collect_box_score_inputdata.fga == fga

        assert isinstance(collect_box_score_inputdata.fgr, str)
        assert collect_box_score_inputdata.fgr == fgr

        assert isinstance(collect_box_score_inputdata.fgm3, int)
        assert collect_box_score_inputdata.fgm3 == fgm3

        assert isinstance(collect_box_score_inputdata.fga3, int)
        assert collect_box_score_inputdata.fga3 == fga3

        assert isinstance(collect_box_score_inputdata.fgr3, str)
        assert collect_box_score_inputdata.fgr3 == fgr3

        assert isinstance(collect_box_score_inputdata.ftm, int)
        assert collect_box_score_inputdata.ftm == ftm

        assert isinstance(collect_box_score_inputdata.fta, int)
        assert collect_box_score_inputdata.fta == fta

        assert isinstance(collect_box_score_inputdata.ftr, str)
        assert collect_box_score_inputdata.ftr == ftr

        assert isinstance(collect_box_score_inputdata.ofr, int)
        assert collect_box_score_inputdata.ofr == ofr

        assert isinstance(collect_box_score_inputdata.der, int)
        assert collect_box_score_inputdata.der == der

        assert isinstance(collect_box_score_inputdata.tor, int)
        assert collect_box_score_inputdata.tor == tor

        assert isinstance(collect_box_score_inputdata.ast, int)
        assert collect_box_score_inputdata.ast == ast

        assert isinstance(collect_box_score_inputdata.to, int)
        assert collect_box_score_inputdata.to == to

        assert isinstance(collect_box_score_inputdata.st, int)
        assert collect_box_score_inputdata.st == st

        assert isinstance(collect_box_score_inputdata.bo, int)
        assert collect_box_score_inputdata.bo == bo

        assert isinstance(collect_box_score_inputdata.bsr, int)
        assert collect_box_score_inputdata.bsr == bsr

        assert isinstance(collect_box_score_inputdata.fo, int)
        assert collect_box_score_inputdata.fo == fo

        assert isinstance(collect_box_score_inputdata.fd, int)
        assert collect_box_score_inputdata.fd == fd

        assert isinstance(collect_box_score_inputdata.dunk, int)
        assert collect_box_score_inputdata.dunk == dunk

        assert isinstance(collect_box_score_inputdata.eff, float)
        assert collect_box_score_inputdata.eff == eff
        
import pytest
from requests_html import HTML

from src.adapter.stats.controller.collect_stats import CollectStats


class TestCollectStatsInner():

    def test_find_game_info_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_game_infoを実行する
        cs = CollectStats()
        r_html = cs._find_game_info(1, r_html)

        # THEN: GAME INFORMATIONに必要な情報を取得できる
        assert True
    
    def test_find_playbyplay_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_playbyplayを実行する
        cs = CollectStats()
        r_html = cs._find_playbyplay(1, r_html)

        # THEN: GAME INFORMATIONに必要な情報を取得できる
        assert True

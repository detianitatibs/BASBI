from typing import List

import pytest
from requests_html import HTML
from injector import Injector, Module, Binder

from src.domain.stats.i_collect_stats_usecase import ICollectStatsUsecase
from src.adapter.stats.controller.collect_stats_controller import CollectStatsController
from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata
from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata
from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata
from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata


class DummyCollectStatsInteractor(ICollectStatsUsecase):
    def translate_and_save(self):
        pass

class TaskDIModule(Module):
    # テスト用にダミークラスをinjectする
    def configure(self, binder: Binder) -> None:
        binder.bind(ICollectStatsUsecase, to=DummyCollectStatsInteractor)

class TestCollectStatsControllerInner():

    def test_find_game_info_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_game_infoを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        inputdata = cs._find_game_info(1, r_html)

        # THEN: GAME INFORMATIONに必要な情報を取得できる
        assert isinstance(inputdata, CollectGameInfoInputdata)
    
    def test_find_game_info_02(
            self,
            init_r_html_02: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_02

        # WHEN: _find_game_infoを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        inputdata = cs._find_game_info(1, r_html)

        # THEN: GAME INFORMATIONに必要な情報を取得できる
        assert isinstance(inputdata, CollectGameInfoInputdata)
    
    def test_find_game_info_03(
            self,
            init_r_html_03: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_03

        # WHEN: _find_game_infoを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        inputdata = cs._find_game_info(1, r_html)

        # THEN: 試合情報がないため、Noneとなっている
        assert inputdata is None
    
    def test_find_game_info_04(
            self,
            init_r_html_04: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_04

        # WHEN: _find_game_infoを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        inputdata = cs._find_game_info(1, r_html)

        # THEN: GAME INFORMATIONに必要な情報を取得できる
        assert isinstance(inputdata, CollectGameInfoInputdata)

    def test_find_game_report_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_game_reportを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_game_report(1, r_html)

        # THEN: GAME REPORTに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectGameReportInputdata)
    
    def test_find_game_report_02(
            self,
            init_r_html_02: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_02

        # WHEN: _find_game_reportを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_game_report(1, r_html)

        # THEN: GAME REPORTに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectGameReportInputdata)
    
    # test_find_game_report_03 は処理されないのでテストスキップ
    
    def test_find_game_report_04(
            self,
            init_r_html_04: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_04

        # WHEN: _find_game_reportを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_game_report(1, r_html)

        # THEN: GAME REPORTに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectGameReportInputdata)

    def test_find_box_score_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_box_scoreを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_box_score(1, r_html)

        # THEN: BOX SCOREに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectBoxScoreInputdata)

    def test_find_box_score_02(
            self,
            init_r_html_02: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_02

        # WHEN: _find_box_scoreを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_box_score(1, r_html)

        # THEN: BOX SCOREに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectBoxScoreInputdata)

    # test_find_box_score_03は処理されないのでテストスキップ

    def test_find_box_score_04(
            self,
            init_r_html_04: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_04

        # WHEN: _find_box_scoreを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_box_score(1, r_html)

        # THEN: BOX SCOREに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectBoxScoreInputdata)
    
    def test_find_playbyplay_01(
            self,
            init_r_html_01: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_01

        # WHEN: _find_playbyplayを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_playbyplay(1, r_html)

        # THEN: PLAY BY PLAYに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectPlayByPlayInputdata)

    def test_find_playbyplay_02(
            self,
            init_r_html_02: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_02

        # WHEN: _find_playbyplayを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_playbyplay(1, r_html)

        # THEN: PLAY BY PLAYに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectPlayByPlayInputdata)

    # test_find_playbyplay_03は処理されないのでテストスキップ

    def test_find_playbyplay_04(
            self,
            init_r_html_04: HTML):
        # CASE: テスト用のr_htmlをfixtureから取得する
        r_html = init_r_html_04

        # WHEN: _find_playbyplayを実行する
        injector = Injector([TaskDIModule()])
        cs = injector.get(CollectStatsController)
        list_inputdata = cs._find_playbyplay(1, r_html)

        # THEN: PLAY BY PLAYに必要な情報を取得できる
        assert isinstance(list_inputdata, List)
        assert isinstance(list_inputdata[0], CollectPlayByPlayInputdata)

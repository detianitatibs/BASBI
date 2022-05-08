import pytest
from requests_html import HTML

from src.adapter.stats.controller.collect_stats import CollectStats


class TestCollectStatsInner():
    """collect_stats.pyの内部関数向けテスト
    """

    @pytest.mark.parametrize('schedule_key', [
        (1)
    ])
    def test_collect_from_web_01(self, schedule_key: int):
        # CASE: 特に無し(今後あるかも)
        # WHEN: _collect_from_webを実行すると
        cs = CollectStats()
        r_html = cs._collect_from_web(schedule_key)

        # requests_html.HTML形式で取得できている
        assert isinstance(r_html, HTML)

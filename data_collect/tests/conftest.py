import os

import pytest
from requests_html import HTML


@pytest.fixture(scope='class')
def init_r_html_01() -> HTML:
    base_dir = os.path.dirname(__file__)
    sample_path = '/'.join([base_dir, 'data/sample_stats_schedule_key_1.txt'])
    # htmlファイルの読み込み
    with open(sample_path) as f:
        html = f.read()
        r_html = HTML(html=html)
    return r_html

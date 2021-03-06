import os

import pytest
from requests_html import HTML


@pytest.fixture(scope='class')
def init_r_html_01() -> HTML:
    base_dir = os.path.dirname(__file__)
    sample_path = '/'.join([base_dir, 'test_data/sample_stats_schedule_key_1.txt'])
    # htmlファイルの読み込み
    with open(sample_path) as f:
        html = f.read()
        r_html = HTML(html=html)
    return r_html

@pytest.fixture(scope='class')
def init_r_html_02() -> HTML:
    base_dir = os.path.dirname(__file__)
    sample_path = '/'.join([base_dir, 'test_data/sample_stats_schedule_key_4094.txt'])
    # htmlファイルの読み込み
    with open(sample_path) as f:
        html = f.read()
        r_html = HTML(html=html)
    return r_html

@pytest.fixture(scope='class')
def init_r_html_03() -> HTML:
    base_dir = os.path.dirname(__file__)
    sample_path = '/'.join([base_dir, 'test_data/sample_stats_schedule_key_4113.txt'])
    # htmlファイルの読み込み
    with open(sample_path) as f:
        html = f.read()
        r_html = HTML(html=html)
    return r_html

@pytest.fixture(scope='class')
def init_r_html_04() -> HTML:
    base_dir = os.path.dirname(__file__)
    sample_path = '/'.join([base_dir, 'test_data/sample_stats_schedule_key_4118.txt'])
    # htmlファイルの読み込み
    with open(sample_path) as f:
        html = f.read()
        r_html = HTML(html=html)
    return r_html

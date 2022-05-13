# 出力結果を>>で出力すること
# 例) python create_sample_data.py -s=X > sample_stats_schedule_key_X.txt
import argparse

from requests_html import HTMLSession, HTML

if __name__ == "__main__":
    # 引数の設定
    parser = argparse.ArgumentParser(description='Bリーグの試合情報を取得する')
    parser.add_argument(
        '-s', '--schedule_key', type=int, help='試合番号'
    )
    args = parser.parse_args()

    url = 'https://www.bleague.jp/game_detail/?ScheduleKey=' + str(args.schedule_key)
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    r_html = r.html
    print(r_html.html)

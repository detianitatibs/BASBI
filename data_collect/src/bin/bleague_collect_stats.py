import argparse
import logging

from injector import Injector

from src.conf.di_module import DIModule
from src.adapter.stats.controller.collect_stats_controller import CollectStatsController


if __name__ == '__main__':
    # ログの設定
    logging.basicConfig(level=logging.INFO)

    # 引数の設定
    parser = argparse.ArgumentParser(description='Bリーグの試合情報を取得する')
    parser.add_argument(
        '-s', '--schedule_key', type=int, help='試合番号'
    )
    args = parser.parse_args()

    # 取得ジョブの実行
    print(args.schedule_key)
    injector = Injector([DIModule()])
    controller = injector.get(CollectStatsController)
    controller.collect(schedule_key=args.schedule_key)

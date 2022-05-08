# BASBI
B league AnalySis BI  
[B LEAGUE](https://www.bleague.jp/)で取得できるデータを活用するための分析基盤  

以下のような機能を持つ
- データ収集機能(data_collect)
    - B LEAGUE公式からデータを取得する機能
    - 取得したデータは`data`ディレクトリに保存する

実行前に、`data_collect`ディレクトリまでのPathを通しておくこと
```
export BASBIPATH="<data_collectまでのパス>";PYTHONPATH="${PYTHONPATH}:${BASBIPATH}"
```

## データ収集機能(data_collect)
- 取得対象データ
    - GAME INFORMATION
        - 試合日や観客数など、試合に関する情報をまとめたデータ
    - GAME REPORT
        - 試合のトータルスタッツをまとめたデータ
    - PLAY BY PLAY
        - クォーターごとに起こったプレーの出来事を時系列に記載したデータ
    - BOX SCORE
        - 個人選手単位の試合のスタッツがまとめられたデータ
- 取得対象期間
    - B LEAGUE発足の2016-17シーズンより最新の値を取得する


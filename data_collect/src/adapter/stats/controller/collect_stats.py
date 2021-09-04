from requests_html import HTMLSession, HTML


class CollectStats():

    def __init__(self):
        # userstoryなどのInterfaceを後で使うスペース
        self.url = 'https://www.bleague.jp/game_detail/?ScheduleKey='
        pass

    def collect(self, schedule_key: int):
        # データを取得して、後続のInteractorに渡すまでを担う箇所
        r_html = self._collect_from_web(schedule_key)
        pass

    def _collect_from_web(self, schedule_key: int) -> HTML:
        self.url = self.url + str(schedule_key)

        # B LEAGUE公式ページからデータをスクレイピングする箇所
        session = HTMLSession()
        r = session.get(self.url)
        r.html.render()
        print(r.html)
        print(type(r.html))
        # print(r.html.find('div#game__highlight', first=True).text)
        # print(r.html.find('div#game__playbyplay', first=True).text)
        # print(r.html.find('div#game__boxscore', first=True).text)
        return r.html

from requests_html import HTMLSession, HTML


class CollectStats():

    def __init__(
            self):
        # userstoryなどのInterfaceを後で使うスペース
        self.url = 'https://www.bleague.jp/game_detail/?ScheduleKey='
        pass

    def collect(
            self,
            schedule_key: int):
        # データを取得して、後続のInteractorに渡すまでを担う箇所
        r_html = self._collect_from_web(schedule_key)
        pass

    def _collect_from_web(
            self,
            schedule_key: int) -> HTML:
        self.url = self.url + str(schedule_key)

        # B LEAGUE公式ページからデータをスクレイピングする箇所
        session = HTMLSession()
        r = session.get(self.url)
        r.html.render()
        print(r.html)
        print(type(r.html))
        # print(r.html.find('div#game__highlight', first=True).text)
        # print(r.html.find('div#game__boxscore', first=True).text)
        return r.html

    def _find_game_info(
            self, schedule_key: int, r_html: HTML):
        date_info = r_html.find('div.date_wrap', first=True)
        s_season = date_info.find('p.year', first=True).text
        s_date = date_info.find('span.month', first=True).text
        s_week = date_info.find('span.week', first=True).text
        s_setsu = date_info.find('span.setsu', first=True).text
        s_tipoff = date_info.find('p.time', first=True).text
        print(s_season)
        print(s_date)
        print(s_week)
        print(s_setsu)
        print(s_tipoff)
        # schedule_keyをPKにして、GAME INFOのinputdataを作るイメージで
    
    def _find_playbyplay(
            self,
            schedule_key: int,
            r_html: HTML):
        playbyplay = r_html.find('div#game__playbyplay', first=True)
        list_timeline = playbyplay.find('li')
        for timeline in list_timeline:
            # time
            time = timeline.find('p.time', first=True)
            s_time = time.text if time is not None else None
            print(s_time)

            # detail
            detail = timeline.find('p.detail', first=True)
            s_detail = detail.text if detail is  not None else None
            print(s_detail)

            print('')

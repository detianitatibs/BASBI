import re
from typing import List
import logging

from requests_html import HTMLSession, HTML
from injector import inject

from src.domain.stats.i_collect_stats_usecase import ICollectStatsUsecase
from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata
from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata
from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata
from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata

logger = logging.getLogger(__name__)


class CollectStatsController():

    @inject
    def __init__(self, interactor: ICollectStatsUsecase):
        # usecaseなどのInterfaceを後で使うスペース
        self.interactor = interactor
        # 共通URL
        self.url = 'https://www.bleague.jp/game_detail/?ScheduleKey='

    def collect(self, schedule_key: int):
        """データ取得

        Webからスクレイピングしたデータを後続のInteractorに渡す

        Args:
            schedule_key (int): 試合番号
        """
        # Webからデータを取得する
        r_html = self._collect_from_web(schedule_key)

        # 各項目に整形して取得する
        game_info_inputdata = self._find_game_info(schedule_key, r_html)
        list_game_report_inputdata = self._find_game_report(schedule_key, r_html)
        list_box_score_inputdata = self._find_box_score(schedule_key, r_html)
        list_play_by_play_inputdata = self._find_playbyplay(schedule_key, r_html)

        # usecaseにinputdataを渡す
        self.interactor.translate_and_save(
            game_info_inputdata,
            list_game_report_inputdata,
            list_box_score_inputdata,
            list_play_by_play_inputdata
        )

    def _collect_from_web(self, schedule_key: int) -> HTML:
        """Webからのデータ取得

        Args:
            schedule_key (int): 試合番号

        Returns:
            HTML: 取得したHTML
        """
        self.url = self.url + str(schedule_key)

        # B LEAGUE公式ページからデータをスクレイピングする
        session = HTMLSession()
        r = session.get(self.url)
        r.html.render()
        logger.debug(r.html)
        logger.debug(type(r.html))
        return r.html

    def _find_game_info(
            self, schedule_key: int, r_html: HTML
        ) -> CollectGameInfoInputdata:
        """game_infoの取得

        Args:
            schedule_key (int): 試合番号
            r_html (HTML): Webから取得してきたHTML
        Reutrns:
            CollectGameInfoInputdata: GameInfoのインプットデータ
        """
        s_title = r_html.find('title', first=True).text

        date_wrap = r_html.find('div.date_wrap', first=True)
        s_tipoff = date_wrap.find('p.time', first=True).text
        s_setsu = date_wrap.find('span.setsu', first=True).text

        place_wrap = r_html.find('div.place_wrap', first=True)
        s_arena = place_wrap.find('p.StadiumNameJ', first=True).text
        s_attendance = place_wrap.find('p.Attendance', first=True).text

        s_refferee = r_html.find('div.referee_wrap', first=True).find('p', first=True).text

        team_wrap_home = r_html.find('div.team_wrap.home', first=True)
        s_home_for_pc = team_wrap_home.find('p.for-pc', first=True).text
        s_home_for_sp = team_wrap_home.find('p.for-sp', first=True).text
        team_wrap_away = r_html.find('div.team_wrap.away', first=True)
        s_away_for_pc = team_wrap_away.find('p.for-pc', first=True).text
        s_away_for_sp = team_wrap_away.find('p.for-sp', first=True).text

        game_score_wrap = r_html.find('div.game_score_wrap', first=True)
        game_score_tr = game_score_wrap.find('tr')
        list_score_home = []
        list_score_away = []
        for tr in game_score_tr:
            quarter_name = tr.find('span.name', first=True).text
            quarter_score_home = tr.find('td.quarter_score.home', first=True).text
            quarter_score_away = tr.find('td.quarter_score.away', first=True).text
            if quarter_name == 'F':
                # 'F'のときはトータルスコアとなる
                total_score_home = int(quarter_score_home)
                total_score_away = int(quarter_score_away)
            else:
                # それ以外のときは、quarterの点数なので、リストに追加する
                list_score_home.append(int(quarter_score_home))
                list_score_away.append(int(quarter_score_away))

        inputdata = CollectGameInfoInputdata(
            schedule_key=schedule_key,
            title=s_title,
            tipoff=s_tipoff,
            sec=s_setsu,
            arena=s_arena,
            attendance=s_attendance,
            referee = s_refferee,
            home_fullname=s_home_for_pc,
            home_name=s_home_for_sp,
            away_fullname=s_away_for_pc,
            away_name=s_away_for_sp,
            home_score=total_score_home,
            home_score_q=list_score_home,
            away_score=total_score_away,
            away_score_q=list_score_away
        )
        logger.debug(inputdata)
        return inputdata
    
    def _find_game_report(
            self, schedule_key: int, r_html: HTML
        ) -> List[CollectGameReportInputdata]:
        """game_reportの取得

        Args:
            schedule_key (int): 試合番号
            r_html (HTML): Webから取得してきたHTML
        Reutrns:
            List[CollectGameReportInputdata]: GameReportのインプットデータ(home/awayでList)
        """
        highlight = r_html.find('div#game__highlight__inner', first=True)
        home_name = highlight.find('div.team_wrap.home', first=True).text
        away_name = highlight.find('div.team_wrap.away', first=True).text

        highlight_tr = highlight.find('tr')
        for tr in highlight_tr:
            value_name = tr.find('td.name', first=True).text
            points = tr.find('td.point')
            if value_name == '2 Points FGM':
                home_fgm = int(points[0].text)
                away_fgm = int(points[1].text)
            elif value_name == '2 Points FGA':
                home_fga = int(points[0].text)
                away_fga = int(points[1].text)
            elif value_name == '2 Points FGR':
                home_fgr = points[0].text
                away_fgr = points[1].text
            elif value_name == '3 Points FGM':
                home_fgm3 = int(points[0].text)
                away_fgm3 = int(points[1].text)
            elif value_name == '3 Points FGA':
                home_fga3 = int(points[0].text)
                away_fga3 = int(points[1].text)
            elif value_name == '3 Points FGR':
                home_fgr3 = points[0].text
                away_fgr3 = points[1].text
            elif value_name == 'Free-ThrowsM':
                home_ftm = int(points[0].text)
                away_ftm = int(points[1].text)
            elif value_name == 'Free-ThrowsA':
                home_fta = int(points[0].text)
                away_fta = int(points[1].text)
            elif value_name == 'Free-ThrowsR':
                home_ftr = points[0].text
                away_ftr = points[1].text
            elif value_name == 'Offensive Rebounds':
                home_ofr = int(points[0].text)
                away_ofr = int(points[1].text)
            elif value_name == 'Defensive Rebounds':
                home_der = int(points[0].text)
                away_der = int(points[1].text)
            elif value_name == 'Total Rebounds':
                home_tor = int(points[0].text)
                away_tor = int(points[1].text)
            elif value_name == 'Assist':
                home_ast = int(points[0].text)
                away_ast = int(points[1].text)
            elif value_name == 'Turnover':
                home_to = int(points[0].text)
                away_to = int(points[1].text)
            elif value_name == 'Steals':
                home_st = int(points[0].text)
                away_st = int(points[1].text)
            elif value_name == 'Blocks':
                home_bo = int(points[0].text)
                away_bo = int(points[1].text)
            elif value_name == 'Fouls':
                home_fo = int(points[0].text)
                away_fo = int(points[1].text)
            elif value_name == 'Fast Break Points':
                home_fbp = int(points[0].text)
                away_fbp = int(points[1].text)
            elif value_name == 'Biggest Lead':
                home_bl = int(points[0].text)
                away_bl = int(points[1].text)
            elif value_name == 'Points in the Paint':
                home_pp = int(points[0].text)
                away_pp = int(points[1].text)
            elif value_name == 'Points From Turnover':
                home_pto = int(points[0].text)
                away_pto = int(points[1].text)
            elif value_name == 'Second Chance Points':
                home_sc = int(points[0].text)
                away_sc = int(points[1].text)
            elif value_name == 'Biggest Scoring Run':
                home_bsr = points[0].text
                away_bsr = points[1].text
            elif value_name == 'Lead Changes':
                lc = int(points[0].text)
            elif value_name == 'Times Tied':
                tt = int(points[0].text)
            
        list_inputdata = []
        home_inputdata = CollectGameReportInputdata(
            schedule_key=schedule_key,
            home_away='H',
            team_name=home_name,
            fgm=home_fgm,
            fga=home_fga,
            fgr=home_fgr,
            fgm3=home_fgm3,
            fga3=home_fga3,
            fgr3=home_fgr3,
            ftm=home_ftm,
            fta=home_fta,
            ftr=home_ftr,
            ofr=home_ofr,
            der=home_der,
            tor=home_tor,
            ast=home_ast,
            to=home_to,
            st=home_st,
            bo=home_bo,
            fo=home_fo,
            fbp=home_fbp,
            bl=home_bl,
            pp=home_pp,
            pto=home_pto,
            scp=home_sc,
            bsr=home_bsr,
            lc=lc,
            tt=tt
        )
        away_inputdata = CollectGameReportInputdata(
            schedule_key=schedule_key,
            home_away='A',
            team_name=away_name,
            fgm=away_fgm,
            fga=away_fga,
            fgr=away_fgr,
            fgm3=away_fgm3,
            fga3=away_fga3,
            fgr3=away_fgr3,
            ftm=away_ftm,
            fta=away_fta,
            ftr=away_ftr,
            ofr=away_ofr,
            der=away_der,
            tor=away_tor,
            ast=away_ast,
            to=away_to,
            st=away_st,
            bo=away_bo,
            fo=away_fo,
            fbp=away_fbp,
            bl=away_bl,
            pp=away_pp,
            pto=away_pto,
            scp=away_sc,
            bsr=away_bsr,
            lc=lc,
            tt=tt
        )
        list_inputdata.append(home_inputdata)
        list_inputdata.append(away_inputdata)
        logger.debug(list_inputdata)
        logger.info('size of game_report list: {}'.format(len(list_inputdata)))
        return list_inputdata

    def _find_box_score(
            self, schedule_key: int, r_html: HTML
        ) -> List[CollectBoxScoreInputdata]:
        """box_scoreの取得

        Args:
            schedule_key (int): 試合番号
            r_html (HTML): Webから取得してきたHTML
        Reutrns:
            List[CollectBoxScoreInputdata]: BoxScoreのインプットデータ
        """
        list_inputdata = []

        html_box_score = r_html.find('ul.boxscore_contents', first=True)
        list_box_score = html_box_score.find('li')
        for box_score in list_box_score:
            team_name ={
                'Home': box_score.find('h2.club-name.Home', first=True).text,
                'Away': box_score.find('h2.club-name.Away', first=True).text
            }
            quoter = box_score.attrs['data-period']

            # tbody(各個人のスタッツ取得)
            tbodies_box_score = box_score.find('tbody')
            for tbody_box_score in tbodies_box_score:
                trs_box_score = tbody_box_score.find('tr')
                for tr_box_score in trs_box_score:
                    data_player_id = tr_box_score.attrs['data-player-id']
                    tds_box_score = tr_box_score.find('td')
                    list_stats = [td_box_score.text for td_box_score in tds_box_score]
                    inputdata = CollectBoxScoreInputdata(
                        schedule_key=schedule_key,
                        # <Element 'tbody' data-period-category='4' class=('Home',)から'class'の1文字目を取得
                        home_away=tbody_box_score.attrs['class'][0][0],
                        team_name=team_name[tbody_box_score.attrs['class'][0]],
                        quoter=quoter,
                        player_id=data_player_id,
                        no=list_stats[0],
                        start_flg=list_stats[1],
                        player_name=tr_box_score.find('span.for-pc', first=True).text,
                        position=list_stats[3],
                        minutes=list_stats[4],
                        pts=int(list_stats[5]),
                        fgm=int(list_stats[6]),
                        fga=int(list_stats[7]),
                        fgr=list_stats[8],
                        fgm3=int(list_stats[9]),
                        fga3=int(list_stats[10]),
                        fgr3=list_stats[11],
                        ftm=int(list_stats[12]),
                        fta=int(list_stats[13]),
                        ftr=list_stats[14],
                        ofr=int(list_stats[15]),
                        der=int(list_stats[16]),
                        tor=int(list_stats[17]),
                        ast=int(list_stats[18]),
                        to=int(list_stats[19]),
                        st=int(list_stats[20]),
                        bo=int(list_stats[21]),
                        bsr=int(list_stats[22]),
                        fo=int(list_stats[23]),
                        fd=int(list_stats[24]),
                        dunk=int(list_stats[25]),
                        eff=float(list_stats[26])
                    )
                    list_inputdata.append(inputdata)

            # tfoot(TEAM/COACHES, 合計の取得)
            # ToDo: tbodyと冗長なので改善する
            tfoots_box_score = box_score.find('tfoot')
            for tfoot_box_score in tfoots_box_score:
                trs_box_score = tfoot_box_score.find('tr')
                for tr_box_score in trs_box_score:
                    data_player_id = tr_box_score.attrs['data-player-id']
                    tds_box_score = tr_box_score.find('td')
                    list_stats = [td_box_score.text for td_box_score in tds_box_score]
                    inputdata = CollectBoxScoreInputdata(
                        schedule_key=schedule_key,
                        # <Element 'tbody' data-period-category='4' class=('Home',)から'class'の1文字目を取得
                        home_away=tbody_box_score.attrs['class'][0][0],
                        team_name=team_name[tbody_box_score.attrs['class'][0]],
                        quoter=quoter,
                        player_id=int(data_player_id) if data_player_id.isdigit() else None,
                        no=int(list_stats[0]) if list_stats[0].isdigit() else None,
                        start_flg=list_stats[1],
                        player_name=list_stats[2],
                        position=list_stats[3],
                        minutes=list_stats[4],
                        pts=int(list_stats[5]),
                        fgm=int(list_stats[6]),
                        fga=int(list_stats[7]),
                        fgr=list_stats[8],
                        fgm3=int(list_stats[9]),
                        fga3=int(list_stats[10]),
                        fgr3=list_stats[11],
                        ftm=int(list_stats[12]),
                        fta=int(list_stats[13]),
                        ftr=list_stats[14],
                        ofr=int(list_stats[15]),
                        der=int(list_stats[16]),
                        tor=int(list_stats[17]),
                        ast=int(list_stats[18]),
                        to=int(list_stats[19]),
                        st=int(list_stats[20]),
                        bo=int(list_stats[21]),
                        bsr=int(list_stats[22]),
                        fo=int(list_stats[23]),
                        fd=int(list_stats[24]),
                        dunk=int(list_stats[25]),
                        eff=float(list_stats[26])
                    )
                    list_inputdata.append(inputdata)

        logger.debug(list_inputdata)
        logger.info('size of box_score list: {}'.format(len(list_inputdata)))
        return list_inputdata
    
    def _find_playbyplay(
            self,
            schedule_key: int,
            r_html: HTML
        ) -> List[CollectPlayByPlayInputdata]:
        """box_scoreの取得

        Args:
            schedule_key (int): 試合番号
            r_html (HTML): Webから取得してきたHTML
        Reutrns:
            List[CollectPlayByPlayInputdata]: PlayByPlayのインプットデータ
        """
        ul_playbyplay = r_html.find('ul.playbyplay_contents.playbyplay_contents_text', first=True)
        lists_playbyplay = ul_playbyplay.find('li')
        list_inputdata = []
        for list_playbyplay in lists_playbyplay:
            # quoterを取得する
            ul = list_playbyplay.find('ul', first=True)
            if ul is not None:
                quoter = ul.attrs['data-period']
            else:
                # quoter以外の情報を取得
                if 'unvisible' in list_playbyplay.attrs['class']:
                    # unvisible列は取得をスキップする
                    continue
                data_no = int(list_playbyplay.attrs['data-no'])
                action_cd = list_playbyplay.attrs['data-action-cd']
                data_class = list_playbyplay.attrs['class']

                # home_awayの取得
                if 'home' in data_class:
                    home_away = 'H'
                elif 'away' in data_class:
                    home_away = 'A'
                elif 'official_time_out' in data_class:
                    home_away = ''

                # flg_pointの取得
                if 'pointup' in data_class:
                    flg_point = True
                else:
                    flg_point = False

                # time_remainingの取得
                time_remaining = list_playbyplay.find('p.time', first=True).text

                # point home/away(ある場合)の取得
                point_home = None
                point_away = None
                points = list_playbyplay.find('p.point', first=True)
                if points is not None:
                    point_home = int(points.text.split('-')[0])
                    point_away = int(points.text.split('-')[1])

                # player_id(ある場合)の取得
                player_id = None
                player_img = list_playbyplay.find('div.player_img', first=True)
                if player_img is not None:
                    style = player_img.attrs['style'].replace(u'\xa0', '')
                    if style != '':
                        background_image = re.search(r'\((.*)\)', style).group(1)
                        player_id = background_image.split('/')[-1].split('_')[0]

                # detailの取得
                details = list_playbyplay.find('p.detail', first=True).text
                inputdata = CollectPlayByPlayInputdata(
                    schedule_key=schedule_key,
                    data_no = data_no,
                    action_cd=action_cd,
                    home_away=home_away,
                    quoter=quoter,
                    time_remaining=time_remaining,
                    flg_point=flg_point,
                    point_home=point_home,
                    point_away=point_away,
                    player_id=player_id,
                    details=details
                )
                list_inputdata.append(inputdata)
        logger.debug(list_inputdata)
        logger.info('size of play_by_play list: {}'.format(len(list_inputdata)))
        return list_inputdata

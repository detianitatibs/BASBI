from typing import List
import logging
from datetime import datetime
import re

from injector import inject

from src.domain.stats.i_collect_stats_usecase import ICollectStatsUsecase
from src.domain.stats.game_info_entity import GameInfoEntity
from src.domain.stats.game_report_entity import GamerReportEntity
from src.domain.stats.box_score_entity import BoxScoreEntity
from src.domain.stats.play_by_play_entity import PlayByPlayEntity
from src.domain.stats.i_game_info_repository import IGameInfoRepository
from src.domain.stats.i_game_report_repository import IGameReportRepository
from src.domain.stats.i_box_score_repository import IBoxScoreRepository
from src.domain.stats.i_play_by_play_repository import IPlayByPlayRepository
from src.application.stats.collect.collect_game_info_inputdata import CollectGameInfoInputdata
from src.application.stats.collect.collect_game_report_inputdata import CollectGameReportInputdata
from src.application.stats.collect.collect_box_score_inputdata import CollectBoxScoreInputdata
from src.application.stats.collect.collect_play_by_play_inputdata import CollectPlayByPlayInputdata

logger = logging.getLogger(__name__)


class CollectStatsInteractor(ICollectStatsUsecase):

    @inject
    def __init__(
        self,
        game_info_repository: IGameInfoRepository,
        game_report_repository: IGameReportRepository,
        box_score_repository: IBoxScoreRepository,
        play_by_play_repository: IPlayByPlayRepository
    ):
        self.game_info_repository = game_info_repository
        self.game_report_repository = game_report_repository
        self.box_score_repository = box_score_repository
        self.play_by_play_repository = play_by_play_repository

    def translate_and_save(
        self,
        schedule_key: int,
        collect_game_info_inputdata: CollectGameInfoInputdata,
        list_collect_game_report_inputdata: List[CollectGameReportInputdata],
        list_collect_box_score_inputdata: List[CollectBoxScoreInputdata],
        list_collect_play_by_play_inputdata: List[CollectPlayByPlayInputdata]
    ) -> None:
        """????????????????????????????????????????????????

        Args:
            schedule_key (int): ????????????
            collect_game_info_inputdata (CollectGameInfoInputdata): GameInfo???????????????????????????
            list_collect_game_report_inputdata (List[CollectGameReportInputdata]): GameRport???????????????????????????
            list_collect_box_score_inputdata (List[CollectBoxScoreInputdata]): BoxScore???????????????????????????
            list_collect_play_by_play_inputdata (List[CollectPlayByPlayInputdata]): PlayByPlay???????????????????????????
        """
        # input->entity???????????????
        game_info_entity = self._translate_game_info(collect_game_info_inputdata)
        list_game_report_entity = self._translate_game_report(list_collect_game_report_inputdata)
        list_box_score_entity = self._translate_box_score(list_collect_box_score_inputdata)
        list_play_by_play_entity = self._translate_play_by_play(list_collect_play_by_play_inputdata)

        # ????????????????????????
        self.game_info_repository.save(schedule_key, game_info_entity)
        self.game_report_repository.save(schedule_key, list_game_report_entity)
        self.box_score_repository.save(schedule_key, list_box_score_entity)
        self.play_by_play_repository.save(schedule_key, list_play_by_play_entity)

    def _translate_game_info(self, inputdata: CollectGameInfoInputdata) -> GameInfoEntity:
        """GameInfo???inputdata??????Entity????????????

        Args:
            collect_game_info_inputdata (CollectGameInfoInputdata): inputdata

        Returns:
            GameInfoEntity: entity
        """
        # ???????????????????????????????????????????????????
        game_date = None
        season = None
        re_game_date = re.search(r'(\d*/\d*/\d*)', inputdata.title)
        if re_game_date is not None:
            d_game_date = datetime.strptime(re_game_date.group(1), '%Y/%m/%d')
            game_date = d_game_date.strftime('%Y-%m-%d')
            # game_date < 6/30???????????????year-1??????game_date > 6/30???????????????year???season?????????
            if d_game_date.month < 7:
                season = str(d_game_date.year - 1)
            else:
                season = str(d_game_date.year)

        division = None
        re_division = re.search(r'(B\d)', inputdata.title)
        if re_division is not None:
            division = re_division.group(1)

        # ??????????????????(HH:MM TIP OFF)???????????????
        tipoff = None
        re_tipoff = re.search(r'(\d*:\d*)', inputdata.tipoff)
        if re_tipoff is not None:
            tipoff = re_tipoff.group(1)

        # ????????????
        sec = None
        if inputdata.sec is not None:
            re_sec = re.search(r'???(\d)???', '???1???')
            sec = int(re_sec.group(1)) if re_sec is not None else None
        
        # ??????????????????
        arena = None
        re_arena = re.search(r'?????????(.*)', inputdata.arena)
        if re_arena is not None:
            arena = re_arena.group(1)
        
        # ??????????????????
        attendance = None
        re_attendance = re.search(r'?????????(\d*)', inputdata.attendance)
        if re_attendance is not None:
            attendance = int(re_attendance.group(1))

        # ????????????????????????
        referee_1 = None
        referee_2 = None
        referee_3 = None
        re_referre = re.search(r'??????????????????(.*)', inputdata.referee)
        if re_referre is not None:
            li_referre = re_referre.group(1).replace('\u3000', ' ').split('???')
            try:
                referee_1 = li_referre[0]
                referee_2 = li_referre[1]
                referee_3 = li_referre[2]
            except Exception:
                logger.warning('out of list error was occurd by referre')

        entity = GameInfoEntity(
            schedule_key=inputdata.schedule_key,
            title=inputdata.title,
            game_date=game_date,
            tipoff=tipoff,
            season=season,
            division=division,
            sec=sec,
            arena=arena,
            attendance=attendance,
            referee_1=referee_1,
            referee_2=referee_2,
            referee_3=referee_3,
            home_fullname=inputdata.home_fullname,
            home_name=inputdata.home_name,
            home_score=inputdata.home_score,
            home_score_q=inputdata.home_score_q,
            away_fullname=inputdata.away_fullname,
            away_name=inputdata.away_name,
            away_score=inputdata.away_score,
            away_score_q=inputdata.away_score_q
        )
        logger.debug(entity)
        return entity
    
    def _translate_game_report(self, list_inputdata: List[CollectGameReportInputdata]) -> List[GamerReportEntity]:
        """GameReport???inputdata??????Entity????????????

        Args:
            list_inputdata (List[CollectGameReportInputdata]): inputdata????????????

        Returns:
            List[GamerReportEntity]: entity????????????
        """
        list_entity = []
        for inputdata in list_inputdata:
            # %??????float????????????????????????
            fgr = self._convert_percent_to_float(inputdata.fgr)
            fgr3 = self._convert_percent_to_float(inputdata.fgr3)
            ftr = self._convert_percent_to_float(inputdata.ftr)
            
            # Biggest Scoring Run?????????
            bsr = inputdata.bsr.replace('\n', ',')
            
            entity = GamerReportEntity(
                schedule_key=inputdata.schedule_key,
                home_away=inputdata.home_away,
                team_name=inputdata.team_name,
                fgm=inputdata.fgm,
                fga=inputdata.fga,
                fgr=fgr,
                fgm3=inputdata.fgm3,
                fga3=inputdata.fga3,
                fgr3=fgr3,
                ftm=inputdata.ftm,
                fta=inputdata.fta,
                ftr=ftr,
                ofr=inputdata.ofr,
                der=inputdata.der,
                tor=inputdata.tor,
                ast=inputdata.ast,
                to=inputdata.to,
                st=inputdata.st,
                bo=inputdata.bo,
                fo=inputdata.fo,
                fbp=inputdata.fbp,
                bl=inputdata.bl,
                pp=inputdata.pp,
                pto=inputdata.pto,
                scp=inputdata.scp,
                bsr=bsr,
                lc=inputdata.lc,
                tt=inputdata.tt
            )
            list_entity.append(entity)
        logger.info('size of game_report list: {}'.format(len(list_entity)))
        logger.debug(list_entity)
        return list_entity

    def _translate_box_score(self, list_inputdata: List[CollectBoxScoreInputdata]) -> List[BoxScoreEntity]:
        """BoxScore???inputdata??????Entity????????????

        Args:
            list_inputdata (List[CollectBoxScoreInputdata]): inputdata????????????

        Returns:
            List[BoxScoreEntithy]: entity????????????
        """
        list_entity = []
        for inputdata in list_inputdata:
            # %??????float????????????????????????
            fgr=self._convert_percent_to_float(inputdata.fgr)
            fgr3=self._convert_percent_to_float(inputdata.fgr3)
            ftr=self._convert_percent_to_float(inputdata.ftr)

            entity = BoxScoreEntity(
                schedule_key=inputdata.schedule_key,
                home_away=inputdata.home_away,
                team_name=inputdata.team_name,
                no=inputdata.no,
                player_id=inputdata.player_id,
                player_name=inputdata.player_name,
                quoter=inputdata.quoter,
                start_flg=inputdata.start_flg,
                position=inputdata.position,
                minutes=inputdata.minutes,
                pts=inputdata.pts,
                fgm=inputdata.fgm,
                fga=inputdata.fga,
                fgr=fgr,
                fgm3=inputdata.fgm3,
                fga3=inputdata.fga3,
                fgr3=fgr3,
                ftm=inputdata.ftm,
                fta=inputdata.fta,
                ftr=ftr,
                ofr=inputdata.ofr,
                der=inputdata.der,
                tor=inputdata.tor,
                ast=inputdata.ast,
                to=inputdata.to,
                st=inputdata.st,
                bo=inputdata.bo,
                bsr=inputdata.bsr,
                fo=inputdata.fo,
                fd=inputdata.fd,
                dunk=inputdata.dunk,
                eff=inputdata.eff
            )
            list_entity.append(entity)
        logger.info('size of box_score list: {}'.format(len(list_entity)))
        logger.debug(list_entity)
        return list_entity

    def _translate_play_by_play(self, list_inputdata: List[CollectPlayByPlayInputdata]) -> List[PlayByPlayEntity]:
        """PlayByPlay???inputdata??????Entity????????????

        Args:
            list_inputdata (List[CollectPlayByPlayInputdata]): inputdata????????????

        Returns:
            List[PlayByPlayEntity]: entity????????????
        """
        list_entity = []
        for inputdata in list_inputdata:
            entity = PlayByPlayEntity(
                schedule_key=inputdata.schedule_key,
                data_no=inputdata.data_no,
                action_cd=inputdata.action_cd,
                home_away=inputdata.home_away,
                quoter=inputdata.quoter,
                time_remaining=inputdata.time_remaining,
                flg_point=inputdata.flg_point,
                point_home=inputdata.point_home,
                point_away=inputdata.point_away,
                details=inputdata.details
            )
            list_entity.append(entity)
        logger.info('size of play_by_play list: {}'.format(len(list_entity)))
        logger.debug(list_entity)
        return list_entity

    def _convert_percent_to_float(self, percent: str) -> float:
        """??????????????????????????????????????????????????????float?????????

        Args:
            percent (str): XX.X%

        Returns:
            float: XX.X
        """
        f_percent = None
        re_percent = re.search(r'(.*)%', percent)
        if re_percent is not None:
            f_percent = float(re_percent.group(1))
        return f_percent


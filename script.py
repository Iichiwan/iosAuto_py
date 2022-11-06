import wda
import time
import logging

from common import Common
from logzero import logger
from checkui import Airtest

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0


class ScriptDemo():
    def summer90pluss(c):
        print("turn1")
        Common.skill(c, 1, 0)
        Common.skill(c, 3, 0)
        Common.skill(c, 5, 1)
        Common.skill(c, 6, 1)
        Common.skill(c, 8, 1)
        Common.skill(c, 9, 1)
        Common.card(c, -1, 1, 2, 16)
        print("turn2")
        Common.skill(c, 4, 0)
        Common.skill(c, 7, 0)
        Common.suitChange(c, 3, 4)
        Common.skill(c, 7, 0)
        Common.card(c, -1, 1, 2, 16)
        print("turn3")
        Common.skill(c, 2, 0)
        Common.skill(c, 8, 1)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 0)
        Common.card(c, -1, 1, 2, 22)
        print("end")
        Common.end(c)

    # 公伽奥
    def GJA(c):
        Common.eatApple(c)
        Common.choose(c)
        logger.info("turn1")
        Common.skill(c, 7, 0)
        Common.skill(c, 8, 1)
        Common.suitSkill(c, 3, 1)
        Common.cardToNextTurn(c, -1, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn2")
        Common.skill(c, 3, 0)
        Common.skill(c, 4, 0)
        Common.skill(c, 5, 0)
        Common.skill(c, 6, 0)
        Common.cardToNextTurn(c, -2, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn3")
        Common.skill(c, 1, 0)
        Common.skill(c, 2, 0)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 1)
        Common.card(c, -1, 1, 2, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    # 种火 绘公奥
    def EXP(c):
        Common.eatApple(c)
        Common.choose(c)
        logger.info("turn1")
        Common.skill(c, 7, 0)
        Common.skill(c, 8, 2)
        Common.suitSkill(c, 3, 2)
        Common.cardToNextTurn(c, -2, 1, 2)
        logger.info("turn2")
        Common.skill(c, 4, 0)
        Common.skill(c, 5, 0)
        Common.cardToNextTurn(c, -2, 1, 2)
        logger.info("turn3")
        Common.skill(c, 1, 0)
        Common.skill(c, 2, 0)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 1)
        Common.card(c, -1, 1, 2, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    # qp 莉公奥
    def QP(c):
        Common.choose(c)
        logger.info("turn1")
        Common.skill(c, 7, 0)
        Common.skill(c, 8, 2)
        Common.suitSkill(c, 3, 2)
        Common.cardToNextTurn(c, -2, 1, 2)
        logger.info("turn2")
        Common.skill(c, 4, 0)
        Common.skill(c, 5, 0)
        Common.cardToNextTurn(c, -2, 1, 2)
        logger.info("turn3")
        Common.skill(c, 1, 0)
        Common.skill(c, 2, 0)
        Common.skill(c, 3, 0)
        Common.skill(c, 6, 0)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 1)
        Common.card(c, -1, 1, 2, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)
        Common.eatApple(c)

    # 活动周回
    def event(c):
        Common.eatApple(c)
        Common.choose(c)
        logger.info("turn1")
        Common.skill(c, 6, 0)
        Common.skill(c, 7, 0)
        Common.skill(c, 8, 1)
        Common.cardToNextTurn(c, -1, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn2")
        Common.skill(c, 1, 0)
        Common.skill(c, 3, 0)
        Common.skill(c, 4, 0)
        Common.skill(c, 5, 0)
        Common.suitSkill(c, 2, 2)
        Common.cardToNextTurn(c, -2, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn3")
        Common.skill(c, 2, 0)
        Common.skill(c, 9, 1)
        Common.card(c, -1, 1, 2, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    # gudaguda90++
    def guda2(c):
        Common.eatApple(c)
        Common.choose(c)
        logger.info("turn1")
        Common.skill(c, 1, 0)
        Common.skill(c, 4, 1)
        Common.skill(c, 6, 1)
        Common.skill(c, 7, 0)
        Common.skill(c, 9, 1)
        Common.suitChange(c, 3, 4)
        Common.skill(c, 7, 0)
        Common.cardToNextTurn(c, -1, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn2")
        Common.skill(c, 2, 0)
        Common.skill(c, 3, 0)
        Common.skill(c, 5, 1)
        # Common.skill(c, 8, 1)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 1)
        Common.card(c, -1, -2, -3, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    # gudaguda90++ 卡莲
    def guda(c):
        Common.eatApple(c)
        Common.choose(c)
        logger.info("turn1")
        #Common.skill(c, 1, 0)
        Common.skill(c, 2, 0)
        Common.skill(c, 3, 0)
        Common.skill(c, 4, 1)
        Common.skill(c, 7, 1)
        Common.skill(c, 8, 0)
        Common.skill(c, 9, 1)
        Common.suitChange(c, 3, 4)
        Common.skill(c, 7, 0)
        Common.cardToNextTurn(c, -1, 1, 2)
        if Airtest.ResultExist():
            Common.waitResult()
            logger.info("end")
            Common.end(c)
            return True
        logger.info("turn2")
        Common.skill(c, 5, 0)
        Common.skill(c, 6, 1)
        Common.skill(c, 8, 1)
        Common.skill(c, 9, 1)
        Common.suitSkill(c, 1, 0)
        Common.card(c, -1, 1, 2, 10)
        Common.waitResult()
        logger.info("end")
        Common.end(c)


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    logging.disable(logging.DEBUG)
    start = time.perf_counter()
    ScriptDemo.GQA(c)
    end = time.perf_counter()
    logger.info("耗时 " + str(round(end - start)) + ' seconds')

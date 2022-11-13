import wda
import json
import requests
import time

from common import Common
from logzero import logger
from checkui import Airtest

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0


def turnEndTest(c):
    if Airtest.ResultExist():
        Common.waitResult()
        logger.info("end")
        Common.end(c)
        return True


class JsonToAuto():

    def read(c, jsonString, times):
        actionJson = json.loads(jsonString);
        for name in actionJson:
            if (name == "start"):
                JsonToAuto.readStart(c, actionJson[name], times);
            if (name == "end"):
                JsonToAuto.readEnd(c, actionJson[name]);
            if ("turn" in name):
                JsonToAuto.readTurn(c, actionJson[name], name);

    def readStart(c, actions, times):
        for action in actions:
            if (action == "eatApple"):
                if (times == 0):
                    continue
                Common.eatApple(c)
                continue
            if (action == "choose"):
                Common.choose(c)
                continue
            if (action["action"] == "eatApple"):
                if (times == 0):
                    continue
                Common.eatApple(c)
                continue
            if (action["action"] == "choose"):
                Common.choose(c)
                continue
            if (action["action"] == "friend"):
                Common.friend(c, action["serClass"], action["serName"])

    def readEnd(c, actions):
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    def readTurn(c, actions, name):
        if (name == "turn2" or name == "turn3"):
            turnEndTest(c);
        print(actions)
        for action in actions:
            if (action['action'] == "skill"):
                Common.skill(c, action["skill"], action["aim"])
            if (action['action'] == "suitSkill"):
                Common.suitSkill(c, action["skill"], action["aim"])
            if (action['action'] == "cardToNextTurn"):
                Common.cardToNextTurn(c, action["one"], action["two"], action["three"])
            if (action['action'] == "suitChange"):
                Common.suitChange(c, action["a"], action["b"])
            if (action['action'] == "card"):
                Common.card(c, action["one"], action["two"], action["three"], action["wait"])
            if (action['action'] == "cardV2"):
                Common.cardV2(c, action["one"], action["two"], action["three"], action["lastTurn"], action["aim"])


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    # 友情池
    for x in range(1000):
        logger.info(x)
        time.sleep(0.5)
        c.click(0.375, 0.575)

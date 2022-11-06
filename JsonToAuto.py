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

    # 公伽奥
    def read(c,jsonString):
        actionJson=json.loads(jsonString);
        for name in actionJson:
            if(name=="start"):
                JsonToAuto.readStart(c,actionJson[name]);
            if(name=="end"):
                JsonToAuto.readEnd(c,actionJson[name]);
            if("turn" in name):
                JsonToAuto.readTurn(c,actionJson[name],name);

    def readStart(c,actions):
        for action in actions:
            if(action=="eatApple"):
                Common.eatApple(c)
            if(action=="choose"):
                Common.choose(c)

    def readEnd(c, actions):
        Common.waitResult()
        logger.info("end")
        Common.end(c)

    def readTurn(c, actions, name):
        if(name=="turn2" or name =="turn3"):
            turnEndTest(c);
        print(actions)
        for action in actions:
            if(action['action']=="skill"):
                Common.skill(c, action["skill"], action["aim"])
            if (action['action'] == "suitSkill"):
                Common.suitSkill(c, action["skill"], action["aim"])
            if (action['action'] == "cardToNextTurn"):
                Common.cardToNextTurn(c, action["one"], action["two"], action["three"])
            if (action['action'] == "suitChange"):
                Common.suitChange(c, action["a"], action["b"])
            if (action['action'] == "card"):
                Common.card(c, action["one"], action["two"], action["three"], action["wait"])


if __name__ == '__main__':
    c=wda.Client('http://localhost:8100')
    url = 'http://116.62.220.225:8080/api/getFgoAuto'
    respose = requests.get(url=url)
    print(respose.text)
    for x in range(10):
        start = time.perf_counter()
        logger.info("开始第 " + str(x + 1) + " 次")
        JsonToAuto.read(c,respose.text);
        end = time.perf_counter()
        logger.info("第 " + str(x + 1) + " 次,耗时 " + str(round(end - start)) + ' seconds')

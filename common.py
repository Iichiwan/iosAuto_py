import wda
import time
wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

from checkui import Airtest



class Common():

    def skill(c,skill,aim):
        # 选技能
        skillx=[0.08,0.136,0.19,0.282,0.338,0.398,0.482,0.54,0.6]
        skilly=0.78

        c.click(skillx[skill-1], skilly)
        time.sleep(0.5)
        # 选目标
        aimx=[0,0.3,0.5,0.7]
        aimy=0.62
        if aim!=0:
            c.click(aimx[aim], aimy)
        # 加速
        Common.quick(c)

    def quick(c):
        c.click(0.088, 0.391)
        c.click(0.088, 0.391)
        time.sleep(0.5)
        c.click(0.088, 0.391)
        c.click(0.088, 0.391)
        time.sleep(0.5)

    def card(c,one,two,three,wait):
        #宝具-1~-3
        #指令卡1~5
        c.click	(0.85, 0.843)
        time.sleep(0.5)
        treax=[0.35,0.5,0.65]
        treay=0.243
        cardx=[0.17,0.34,0.5,0.66,0.83]
        cardy=0.656
        if one<0:
            c.click(treax[one*-1-1],treay)
        else:
            c.click(cardx[one-1],cardy)
        time.sleep(0.3)
        if two<0:
            c.click(treax[two*-1-1],treay)
        else:
            c.click(cardx[two-1],cardy)
        time.sleep(0.3)
        if three<0:
            c.click(treax[three*-1-1],treay)
        else:
            c.click(cardx[three-1],cardy)
        for x in range(wait):
            Common.quick(c)

    #非最终回合回合出卡
    def cardToNextTurn(c,one,two,three):
        #宝具-1~-3
        #指令卡1~5
        c.click	(0.85, 0.843)
        time.sleep(0.5)
        treax=[0.35,0.5,0.65]
        treay=0.243
        cardx=[0.17,0.34,0.5,0.66,0.83]
        cardy=0.656
        if one<0:
            c.click(treax[one*-1-1],treay)
        else:
            c.click(cardx[one-1],cardy)
        time.sleep(0.3)
        if two<0:
            c.click(treax[two*-1-1],treay)
        else:
            c.click(cardx[two-1],cardy)
        time.sleep(0.3)
        if three<0:
            c.click(treax[three*-1-1],treay)
        else:
            c.click(cardx[three-1],cardy)
        for x in range(10):
            Common.quick(c)
        #等待至下一回合开始
        for x in range(10):
            if Airtest.AttackExist():
                break
            if Airtest.ResultExist():
                break

    #等待结果
    def waitResult():
        for x in range(10):
            if Airtest.ResultExist():
                break

    def suitChange(c,a,b):
        #选择换人技能
        c.click(0.9, 0.443)
        time.sleep(0.5)
        c.click(0.83, 0.43)
        time.sleep(0.5)
        #换人界面
        teamx=[0.17,0.3,0.43,0.56,0.69,0.82]
        teamy=0.5
        c.click(teamx[a-1], teamy)
        time.sleep(0.3)
        c.click(teamx[b-1], teamy)
        time.sleep(0.5)
        c.click(0.498, 0.878)
        Common.quick(c)
        Common.quick(c)

    #御主技能
    def suitSkill(c, skill, aim):
        #打开衣服
        c.click(0.9, 0.443)
        time.sleep(0.5)
        #技能
        suitx=[0.72,0.775,0.83]
        suity=0.434
        c.click(suitx[skill-1],suity)
        time.sleep(0.5)
        # 选目标
        aimx=[0,0.3,0.5,0.7]
        aimy=0.62
        if aim!=0:
            c.click(aimx[aim], aimy)
        # 加速
        Common.quick(c)

    #结束战斗
    def end(c):
        Common.quick(c)
        c.click(0.802, 0.891)
        time.sleep(0.5)
        c.click(0.802, 0.891)
        time.sleep(0.5)
        c.click(0.294, 0.852)
        time.sleep(0.5)
        c.click(0.628, 0.786)

    #吃苹果
    def eatApple(c):
        c.click(0.528, 0.447)
        time.sleep(0.5)
        c.click(0.63, 0.773)
        time.sleep(4)

    #选人等待进战
    def choose(c):
        c.click(0.528, 0.447)
        # 等待至下一回合开始
        for x in range(10):
            if Airtest.AttackExist():
                break

    #选择关卡
    def start(c):
        for x in range(5):
            if Airtest.MainPage():
                break
            Common.quick(c)
        c.click(0.742, 0.213)
        time.sleep(2)
        if Airtest.NoAP():
            Common.eatApple(c)
        c.click(0.528, 0.447)
        time.sleep(2)
        c.click(0.928, 0.913)
        # 等待至下一回合开始
        for x in range(10):
            if Airtest.AttackExist():
                break





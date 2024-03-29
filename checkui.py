import logging
import sys

from airtest.core.api import *


class Airtest():

    # 公伽奥
    def AttackExist():
        #auto_setup(__file__, devices=["iOS:///http://127.0.0.1:8100"])
        if exists(Template(r"pics/tpl1660997549383.png", record_pos=(0.351, 0.155), resolution=(2436, 1125))):
            logging.info("find attack")
            return True

    def ResultExist():
        if (exists(Template(r"pics/tpl1660999062281.png", record_pos=(0.351, 0.155), resolution=(2436, 1125)))):
            logging.info("find result")
            return True

    def MainPage():
        if exists(Template(r"pics/tpl1661019951736.png", record_pos=(0.385, 0.185), resolution=(2436, 1125))):
            logging.info("find mainpage")
            return True

    def NoAP():
        if exists(Template(r"pics/tpl1661085288830.png", record_pos=(-0.002, -0.19), resolution=(2436, 1125))):
            logging.info("find NoAP")
            return True
        return False

    def SerAssKeyang():
        if exists(Template(r"pics/tpl1668012867694.png", record_pos=(0.184, -0.018), resolution=(2436, 1125))):
            logging.info("find AssKeyang")
            return True
        return False

    def SelectAssKeyang():
        touch(Template(r"pics/tpl1668012867694.png", record_pos=(0.184, -0.018), resolution=(2436, 1125)))

    def SerABL():
        sys.setrecursionlimit(1000000)
        if exists(
                Template(r"pics/tpl1668248182803.png", rgb=True, record_pos=(0.181, -0.017), resolution=(2436, 1125),
                         threshold=0.85)):
            logging.info("find AssABL")
            return True
        return False

    def SelectABL():
        touch(Template(r"pics/tpl1668248182803.png", rgb=True, record_pos=(0.181, -0.017), resolution=(2436, 1125),
                       threshold=0.85))

    def SerABL5():
        if exists(
                Template(r"pics/tpl1668253545388.png", rgb=True, record_pos=(-0.11, -0.022), resolution=(2436, 1125))):
            logging.info("find AssABL")
            return True
        return False

    def SelectABL5():
        touch(Template(r"pics/tpl1668253545388.png", rgb=True, record_pos=(-0.11, -0.022), resolution=(2436, 1125)))

    def SerCaber():
        if exists(
                Template(r"pics/tpl1685179949720.png", rgb=True, record_pos=(-0.11, -0.022), resolution=(2436, 1125))):
            logging.info("find Caber")
            return True
        return False
    def SelectCaber():
        touch(Template(r"pics/tpl1685179949720.png", rgb=True, record_pos=(-0.11, -0.022), resolution=(2436, 1125)))



if __name__ == '__main__':
    Airtest.AttackExist();

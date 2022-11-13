# This is a sample Python script.
import time

import wda
import requests

from script import ScriptDemo
from logzero import logger
from JsonToAuto import JsonToAuto


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 替换此处id为脚本对应id
    id = "28";
    c = wda.Client('http://localhost:8100')
    url = 'http://116.62.220.225:8080/api/getFgoAuto?id=' + id;
    respose = requests.get(url=url)
    print(respose.text)
    for x in range(20):
        start = time.perf_counter()
        logger.info("开始第 " + str(x + 1) + " 次")
        JsonToAuto.read(c, respose.text, x);
        end = time.perf_counter()
        logger.info("***");
        logger.info("***");
        logger.info("***");
        logger.info("==============================================================================================================第 " + str(x + 1) + " 次,耗时 " + str(round(end - start)) + ' seconds==============================================================================================================')
        logger.info("***");
        logger.info("***");
        logger.info("***");

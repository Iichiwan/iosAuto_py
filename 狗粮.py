import wda
import time

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

from checkui import Airtest
from logzero import logger


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    # 狗粮
    for x in range(1000):
        logger.info(x)
        #c.click(0.87, 0.23)
        time.sleep(0.5)
        c.click(0.55, 0.9)
        time.sleep(0.5)
        c.click(0.9, 0.9)
        time.sleep(0.5)
        c.click(0.6, 0.85)
        time.sleep(0.5)

        for x in range(10):
            c.click(0.55, 0.9)
            time.sleep(0.2)

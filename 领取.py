import wda
import time

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

from checkui import Airtest
from logzero import logger


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    # 无限池
    for x in range(1000):
        logger.info(x)
        c.click(0.5, 0.5)
        time.sleep(0.5)


import wda
import time

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

from checkui import Airtest
from logzero import logger


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    # 友情池
    for x in range(1000):
        c.click(0.572, 0.908)
        time.sleep(0.1)
        c.click(0.62, 0.778)
        time.sleep(6)
        c.click(0.62, 0.778)
        c.click(0.62, 0.778)
        time.sleep(1)
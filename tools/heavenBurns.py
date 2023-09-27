import wda
import time
from logzero import logger

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 180.0  # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0


if __name__ == '__main__':
    c = wda.Client('http://localhost:8100')
    # 友情池
    for x in range(10000):
        c.click(0.6, 0.7)
        time.sleep(0.1)
        c.click(0.6, 0.4)
        time.sleep(0.1)
        c.click(0.6, 0.8)
        logger.info(str(x + 1))
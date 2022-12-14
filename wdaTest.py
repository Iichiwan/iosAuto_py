import wda
import time
wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

class TestDemo():
    def setup(self):
        self.c = wda.USBClient("00008101-000255021E08001E", port=8100)
        self.c.wait_ready(timeout=300)
        self.c.implicitly_wait(30.0)

    def teardown(self):
        self.c.session().app_terminate("com.apple.Preferences")

    def test_NFC(self):
        self.c.session('com.apple.Preferences')
        self.c.swipe_down()

        self.c(name="搜索").set_text("NFC")  # 搜索 NFC
        self.c(name="NFC").click()  # 点击NFC
        time.sleep(1)

        ele = self.c(xpath='//Switch').wait(timeout=3.0)
        sw = ele.value
        if sw == '1':
            ele.click()
            self.c.alert.wait(3)
            self.c.alert.click("关闭")
            time.sleep(1)
            sw = ele.value

        assert sw == '0'

    def test_NFC(c):
        c.session('com.apple.Preferences')
        c.swipe_down()

        c(name="搜索").set_text("NFC")  # 搜索 NFC
        c(name="NFC").click()  # 点击NFC
        time.sleep(1)

        ele = c(xpath='//Switch').wait(timeout=3.0)
        sw = ele.value
        if sw == '1':
            ele.click()
            c.alert.wait(3)
            c.alert.click("关闭")
            sleep(1)
            sw = ele.value

        assert sw == '0'
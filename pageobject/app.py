from pageobject.base_page import BasePage
from appium import webdriver

class App(BasePage):
    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"  # api 23
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "uiautomator2"
        """
        Android 不同版本的系统对应着不同
        """
        caps["chromedriverExecutable"] = "/Users/zhengbangbo/tools/chromedriver/2.20/chromedriver"

        # 加快速度的配置
        # caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["skipServerInstallation"] = True
        # caps["skipLogcatCapture"] = True
        # caps["skipUnlock"] = True
        # caps["skipDeviceInitialization"] = True
        # caps["noSign"] = True

        # 键盘相关
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Home(self.driver)

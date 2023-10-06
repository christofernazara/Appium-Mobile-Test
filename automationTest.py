from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options
import time 

option = UiAutomator2Options()
option.udid = 'emulator-5554'
option.app_package = 'com.millenialzdev.mylogin'
option.app_activity = 'com.millenialzdev.mylogin.MainActivity'
option.platform_name = 'Android'
# desired_caps = {}

# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = 'virtualdevice'
# desired_caps['appPackage'] = 'com.millenialzdev.mylogin'
# desired_caps['appActivity'] = 'com.millenialzdev.mylogin.MainActivity'
# desired_caps['noReset'] = True




driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=option)

#Positive Case When User Fill Username and Password 
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').send_keys("Millenialz Dev");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').send_keys("Admin");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/btnLogin').click();
time.sleep(5)
driver.back();
#Negative Case When User Fill Username and Password Blank
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').clear();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').clear();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').send_keys("");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').send_keys("");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/btnLogin').click();
time.sleep(5)
driver.back();
#Negative Case When User Fill Username without password
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').clear();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').clear();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etUsername').send_keys("Millenialz Dev");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').click();
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/etPassword').send_keys("");
driver.find_element(by=AppiumBy.ID, value= 'com.millenialzdev.mylogin:id/btnLogin').click();

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import telebot
from telebot import types

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


TOKEN = "2003097102:AAHcvmuMAIPRNzlKRfVFMsjegOQIOYUslfw"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "<b>ну здарова ебать)</b>", parse_mode='html')
    print(message.chat.id)

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("https://binarium.global")
time.sleep(20)
search = driver.find_element_by_xpath(
#    "/html/body/app-client/div/ng-component/app-sidebar/div/app-signup-header/div/div/div[1]/button[1]")
#search.click()
time.sleep(10)
googleButton = driver.find_element_by_xpath(
    "/html/body/app-client/div/ng-component/app-sidebar/div/app-signup-social/div/div/div/a[3]")
googleButton.click()
time.sleep(10)
globalWindow = driver.window_handles[0]
authWindow = driver.window_handles[1]
driver.switch_to.window(authWindow)
time.sleep(10)
googleAuthFirst = driver.find_element_by_xpath('//*[@id="identifierId"]')
googleAuthFirst.send_keys("dimamatvej729")
googleAuthFirst.send_keys(Keys.ENTER)
time.sleep(10)
googleAuthSecond = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
googleAuthSecond.send_keys("qwertyuiop2105")
googleAuthSecond.send_keys(Keys.ENTER)
driver.switch_to.window(globalWindow)
time.sleep(11)
driver.get("https://binarium.global/terminal")
time.sleep(10)
driver.find_element_by_xpath("//body").click()
tradingRoomButton = driver.find_element_by_xpath(
    '//*[@id="terminal"]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[4]/div')
try:
    tradingRoomButton.click()
except:
    tradingRoomButton.click()
signalsList = driver.find_element_by_xpath(
    '//*[@id="terminal"]/div[1]/div[1]/div[2]/div[3]/div[4]/div/div/div[3]/div/div[2]/div')
cmpSignal = driver.find_element_by_class_name("signal__text")
bot.send_message(-547367698, "bot is working...")
while True:
    time.sleep(30)
    lastSignal = driver.find_element_by_class_name("signal__text")
    if cmpSignal != lastSignal:
        cmpSignal = lastSignal
        bot.send_message(-547367698, lastSignal.text)
    else:
        bot.send_message(-547367698, "nothing's changed")




bot.polling(none_stop = True)

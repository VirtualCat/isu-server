from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def loginin(user_id,user_pass):
    url = 'https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU'
    url2 = 'https://ci.isu.edu.tw/prev/prev_fill.asp'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    #browser = webdriver.Chrome()
    browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

    browser.get(url)
    browser.implicitly_wait(2)

    elem=browser.find_element_by_name('loginID')
    elem.send_keys(user_id)
    elem=browser.find_element_by_name('passID')
    elem.send_keys(user_pass)
    elem.send_keys(Keys.ENTER)
    browser.implicitly_wait(5)

    browser.get(url2)
    browser.implicitly_wait(2)

    fill = browser.find_element_by_id('nav_bar_txt1').click()
    browser.implicitly_wait(2)
    check = browser.find_element_by_id('emp_past14_10').click()
    sumbit = browser.find_element_by_id('submit_btn').click()

    browser.quit()

f1 = open('.\\log\\user.txt', 'r', encoding='utf-8')
f2 = open('.\\log\\pass.txt', 'r', encoding='utf-8')

l1 = [(line.strip()).split() for line in f1]
l2 = [(line.strip()).split() for line in f2]

for i in range(len(l1)):
    loginin(l1[i],l2[i])   
    print("OK")
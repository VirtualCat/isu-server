from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU'
url2 = 'https://ci.isu.edu.tw/prev/prev_fill.asp'

user = 'isu10603017a'
password = 'howard990523'


#user = ''
#password = ''

### chrome undiplay setting
options = webdriver.ChromeOptions()
options.add_argument('--headless')

#### display
#browser = webdriver.Chrome()
#### undisplay
browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

#### url
browser.get(url)
browser.implicitly_wait(2)

### loging
elem=browser.find_element_by_name('loginID')
elem.send_keys(user)
elem=browser.find_element_by_name('passID')
elem.send_keys(password)
elem.send_keys(Keys.ENTER)
browser.implicitly_wait(5)

browser.get(url2)
browser.implicitly_wait(2)

### autofill
## 畫面過大時id為 nav_bar_txt2 
fill = browser.find_element_by_id('nav_bar_txt1').click()
browser.implicitly_wait(2)
check = browser.find_element_by_id('emp_past14_10').click()
sumbit = browser.find_element_by_id('submit_btn').click()

### close
browser.quit()
# # starter code https://stackoverflow.com/a/40325895/10699882

import time
from selenium import webdriver

chromedriver_path = r"C:\Users\Parker\Desktop\chromedriver.exe"
#create webdriver object and get url
driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(1)
driver.get('https://www.runitonce.com/vision/')

# wait a little bit for me to login to RIO
time.sleep(45)


# find cards
foo = driver.find_element_by_id('intro-text')
foo.find_elements_by_class_name('result-hand-graphical')

# store cards in empty list
cards = []

# grabs card image file path names
for i in foo.find_elements_by_class_name('result-hand-graphical'):
	cards.append(i.get_attribute('src'))


# empty list to store hand
hand = []
for card in cards:
    hand.append(card.replace(r"https://www.runitonce.com/static/img/visions/card-set/", "").replace(r".png?2.0", ""))


# grab result and print text
result = driver.find_element_by_id('practice-result')
print(result.text)

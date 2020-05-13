# # # starter code https://stackoverflow.com/a/40325895/10699882

import time
from selenium import webdriver
import xlwt 
from xlwt import Workbook

chromedriver_path = r"C:\Users\Parker\Desktop\chromedriver.exe"
#create webdriver object and get url
driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(1)
driver.get('https://www.runitonce.com/vision/')

# wait a bit so I can log into Run It Once
time.sleep(45)

wb = Workbook() 
sheet1 = wb.add_sheet('100bb SRP COvsBTN')
sheet1.write(0, 0, 'Board')
sheet1.write(0, 1, 'Hand')
sheet1.write(0, 2, 'Result') 
counter = 1


def reverse(s): 
  string = "" 
  for i in s: 
    string = i + string
  return string


def scrape_vision():
    scenario = driver.find_element_by_id('board-header').text
    board = driver.find_element_by_class_name('board').get_attribute('data-texture')

    # find cards
    foo = driver.find_element_by_id('intro-text')
    cards = []  # store cards in empty list

    # grabs image file path for our cards
    for i in foo.find_elements_by_class_name('result-hand-graphical'):
        cards.append(i.get_attribute('src'))

    hand = []
    for card in cards:
        hand.append(card.replace(r"https://www.runitonce.com/static/img/visions/card-set/", "").replace(r".png?2.0", "").replace('/', ''))
    # move suit to right side of card 
    for card in range(len(hand)):
        hand[card] = reverse(hand[card])

    # grab result and print text
    result = driver.find_element_by_id('practice-result')
    if result.text:
        # write results in workbook
        global counter
        sheet1.write(counter, 0, board)
        sheet1.write(counter, 1, hand)
        sheet1.write(counter, 2, result.text)
        counter += 1
        
        print(result.text)
        print(hand)

        if counter > 25:
            # save results to workbook
            wb.save('results.xls') 


def check_for_left_click():
    # Code to check if left or right mouse buttons were pressed
    import win32api
    import time

    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

    while True:
        a = win32api.GetKeyState(0x01)

        if a != state_left:  # Button state changed
            state_left = a
            # print(a)
            if a < 0:
                # print('Left Button Pressed')
                time.sleep(0.2)
                scrape_vision()
                
        time.sleep(0.001)


check_for_left_click()
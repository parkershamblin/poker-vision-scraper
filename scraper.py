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


# create excel workbook to store results
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1')
# write column headers
sheet1.write(0, 0, 'Hand') 
sheet1.write(0, 1, 'Result') 
# counter to enumerate results in workbook
counter = 1


def scrape_vision():
    # find cards
    foo = driver.find_element_by_id('intro-text')
    foo.find_elements_by_class_name('result-hand-graphical')
    cards = []  # store cards in empty list

    # grabs image file path for our cards
    for i in foo.find_elements_by_class_name('result-hand-graphical'):
        cards.append(i.get_attribute('src'))

    # empty list to store hand
    hand = []
    for card in cards:
        hand.append(card.replace(r"https://www.runitonce.com/static/img/visions/card-set/", "").replace(r".png?2.0", ""))

    # grab result and print text
    result = driver.find_element_by_id('practice-result')
    if result.text:
        # write results in workbook
        global counter
        sheet1.write(counter, 0, hand)
        sheet1.write(counter, 1, result.text)
        counter += 1
        
        print(result.text)
        print(hand)

        if counter > 10:
            # save results to workbook
            wb.save('vision_results.xls') 


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
                scrape_vision()
                
        time.sleep(0.001)


check_for_left_click()
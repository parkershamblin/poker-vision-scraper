# Input your Run It Once Log In Details here.
username_input = "ENTER YOUR USERNAME HERE"
password_input = "ENTER YOUR PASSWORD HERE"

import time
import win32api
from os import path
from selenium import webdriver
from openpyxl import Workbook
from openpyxl import load_workbook


# Load workbook if it exist and if not create new workbook.
if path.exists('RIO-Vision-Results.xlsx'):
    wb = load_workbook('RIO-Vision-Results.xlsx')
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.title = 'RIO-Vision-Results'
    ws['A1'] = 'Line'
    ws['B1'] = 'Overview'
    ws['C1'] = 'Board'
    ws['D1'] = 'Hand'
    ws['E1'] = 'Result'


chromedriver_path = r"C:\Users\Parker\Desktop\chromedriver.exe"
#create webdriver object and get url
driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(1)
driver.get('https://www.runitonce.com/login/?next=/vision/')


# wait a bit for Run It Once to load and allow us to login
# if your computer or internet is slow you might want to increase
# this number from 7 to 10-14
time.sleep(7)

# log into Run It Once
username = driver.find_element_by_id('login-username')
username.clear()
username.send_keys(username_input)
password = driver.find_element_by_id('login-password')
password.clear()
password.send_keys(password_input)
driver.find_element_by_class_name('login-btn').click()


previous_result = ""


def reverse(s): 
  string = "" 
  for i in s: 
    string = i + string
  return string


def scrape_vision():
    line = driver.find_element_by_id('board-header').text
    board = driver.find_element_by_class_name('board').get_attribute('data-texture')

    # find cards
    foo = driver.find_element_by_id('intro-text')
    cards = []  # store cards in empty list

    try:
        # grabs image file path for our cards
        for i in foo.find_elements_by_class_name('result-hand-graphical'):
            cards.append(i.get_attribute('src'))

        hand = []
        for card in cards:
            hand.append(card.replace(r"https://www.runitonce.com/static/img/visions/card-set/", "").replace(r".png?2.0", "").replace('/', ''))
        # move suit to right side of card 
        for card in range(len(hand)):
            hand[card] = reverse(hand[card])
        # covert hand from list to string
        hand = ''.join(hand[:])

        # grab result and print text
        result = driver.find_element_by_id('practice-result')
        if result.text:

            # prevents duplicate results being written to worksheet when a user clicks while on the results page
            global previous_result
            if result.text != previous_result:
                # TODO Fix issue with situation not being included in first hand result
                # have to click on overview tab to get overview text
                driver.find_element_by_id('overview-tab').click()
                situation = driver.find_element_by_id('hand-graph-title-overview').text
                # click back to situation tab so that user doesn't have to do it each time
                driver.find_element_by_id('situation-tab').click()

                # write results in workbook
                ws.append([line, situation, board, hand, result.text])
                # save results to workbook
                wb.save('RIO-Vision-Results.xlsx') 

                previous_result = result.text
                
                print(result.text)
                print(hand)
    except Exception as e:
        print(f"An error occured. Here is the error: {e}")
        pass


def check_for_left_click():
    # Code to check if left or right mouse buttons were pressed

    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

    while True:
        a = win32api.GetKeyState(0x01)

        if a != state_left:  # Button state changed
            state_left = a
            # print(a)
            if a < 0:
                # print('Left Button Pressed')
                time.sleep(0.05)
                scrape_vision()
                
        time.sleep(0.001)


check_for_left_click()
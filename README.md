# vision-scraper

Scraper for Run It Once [Vision](https://www.runitonce.com/vision/). This scraper currently only works on Windows.

# Instructions:
1. Download the [vision-scraper repo](https://github.com/parkershamblin/vision-scraper/archive/master.zip).

2. Download [Chrome Driver v81](https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_win32.zip)

3. Download the [lastest version Python](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe).

4. Download [Sublime Text 3 for Windows 64](https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe) or [Sublime Text 3 for Windows 32 bit](https://download.sublimetext.com/Sublime%20Text%20Build%203211%20Setup.exe).
5. Open up the folder for this repo which you downloaded in step one and type 'cmd' in the search bar then run 'pip install -r requirements.txt'
![image](https://user-images.githubusercontent.com/53675680/82123878-ccb51080-9769-11ea-9555-d8cb93981946.png)
![image](https://user-images.githubusercontent.com/53675680/82123925-0128cc80-976a-11ea-9be0-12f373b5bd79.png)

6. Now click on the 'scraper.py' file and click 'open with' and choose 'Sublime Text'. If 'Sublime Text' does not appear then click 'Choose another app' and select 'Sublime Text' from the option list. If 'Sublime text' does not appear in that option list then click 'More apps' then 'Look for another app on this PC' and go to where you download Sublime Text and select it. ![image](https://user-images.githubusercontent.com/53675680/82124358-9af17900-976c-11ea-9ad8-8b1720fb467a.png)

7. In the 'scraper.py' file enter in your chrome driver file path by Shift Right Clicking the Chrome Driver exe file you downloaded in step 2.![image](https://user-images.githubusercontent.com/53675680/82146586-5c65c800-9819-11ea-960f-538c8e40a285.png) ![image](https://user-images.githubusercontent.com/53675680/82147047-101b8780-981b-11ea-8e4e-d84794fe0e10.png)

8. Next enter in your Run It Once username and password.

9. Finally hit 'Ctrl + B' with Sublime Text open to run the scraper. It will log you in automatically and once you begin to play hands it will store the results in an excel file titled 'RIO-Vision-Results.xlsx', which will be stored in the vision-scraper repo folder that you installed in step 1.


Your results should look something like the following:
![image](https://user-images.githubusercontent.com/53675680/82147360-2fb3af80-981d-11ea-8aa2-861432a5e0a0.png)

# Issues
1. It appears that if you click on "new hand" as soon as it appears on your screen the results text will not properly save to Excel. Try waiting at least one second after playing a hand before moving onto the next one.
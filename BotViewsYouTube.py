import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

full_cmd_arguments = sys.argv
args = full_cmd_arguments[1:]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#CHECKS STEPS
done = False
steps = 0
maxSteps = 1
def next():
    global steps, done
    if steps == maxSteps:
        done = True
        return
    steps += 1

try:
    while done == False:
        print('==ITERATE==')
        #
        if steps == 0:
            print('==STEP0==')
            driver1 = webdriver.Chrome(ChromeDriverManager().install())
            driver1.get('https://www.youtube.com/watch?v=t_Kd_G7p6ZQ')
            btnVideo = driver1.find_element(By.CSS_SELECTOR, "#vjs_video_3_html5_api")
            btnVideo.click()
            btnPlay1 = driver1.find_element(By.CSS_SELECTOR, "#vjs_video_3 > button")
            btnPlay1.click()
            time.sleep(2.0)
            next()
        elif steps == 1:
             print('==STEP0==')
             driver2 = webdriver.Chrome(ChromeDriverManager().install())
             driver2.get('https://www.youtube.com/watch?v=t_Kd_G7p6ZQ')
             btnPlay2 = driver2.find_element(By.CSS_SELECTOR, "#vjs_video_3 > button")
             btnPlay2.click()
             time.sleep(2.0)
             next()
    time.sleep(1)
    next()
    #
except:
    print('Ocorreu um erro.') 
    #
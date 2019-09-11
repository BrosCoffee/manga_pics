from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import urllib
import math
from pics_method import Pics
import os

def get_manga(manga_index, chapter_index):
    start = time.time()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)  # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
      
    try:
        url = 'https://www.8899.click/online/comic-' + str(manga_index) + '.html?ch=' + str(chapter_index)
        driver.get(url)
        count = 1
        html, driver = Pics.get_pics(manga_index, chapter_index, url, driver, count)

        page_start_index = int(html.find('第1/')) + 3
        page_end_index = page_start_index + 2
        total_page_num = int(html[page_start_index:page_end_index])  # Received the total pages of this chapter

        for i in range(2, total_page_num + 1):
            url_ext = url + '-' + str(i)
            driver.get(url_ext)
            count += 1 
            Pics.get_pics(manga_index, chapter_index, url, driver, count)

        driver.close()  # 關掉Driver打開的瀏覽器
        end = time.time()
        second = math.floor((end - start) % 60)
        minute = math.floor((end - start - second) / 60)
        avg = round((end - start) / total_page_num, 3)
        print('Finished')
        print('Total time:', minute, 'm', second, 's')
        print('Avg. time:', avg, 's')
    except:
        print('輸入有錯喔! (Incorrect index entered)')
        driver.close()
        cmd = 'cd ..; rm -rf ' + str(chapter_index)
        os.system(cmd)
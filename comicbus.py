from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import urllib
import math
import os
import sys

def get_manga(manga_index, chapter_index, folder):
    start = time.time()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)  # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
      
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
        print('Total time:', minute, 'm', second, 's')
        print('Avg. time:', avg, 's')
        print('完成 請關閉程式 (Finished, please turn off the app.)')
    except:
        cmd = 'cd ' + folder + '; rm -rf ' + str(chapter_index)
        os.system(cmd)
        print('輸入有錯喔! (Incorrect index entered)')
        print('請重新啟動程式 (Please reactivate the app.)')
        driver.close()

class Pics:
    def get_pics(manga_index, chapter_index, url, driver, count):
       
        def tryclick(driver, selector, count=0):
            try:
                elem = driver.find_element_by_css_selector(selector)
                elem.click()  # 點擊定位到的元素
            except:
                count += 1
                if (count < 2):
                    tryclick(driver, selector, count)

        tryclick(driver, "#flang > option:nth-child(2)")  # 設定成中文
        tryclick(driver, "#crstime_search")  # 點擊「檢索」按鍵
               
        html = driver.page_source  # 取得html文字
        # Find the pic and download it
        # Determine which manga the user is interested, extendable.
        # print(html)
        def code(manga_index, chapter_index):
            if manga_index == '103': # One Piece: 103
                return 'img3.8comic.com/2/'
            elif manga_index == '102': # Naruto: 102
                return 'img3.8comic.com/2/'
            elif manga_index == '10406': # One Punch Man: 10406            
                if int(chapter_index) >= 157 or int(chapter_index) == 154: 
                    return 'img3.8comic.com/3/'
                elif int(chapter_index) >= 151 and int(chapter_index) <= 153:
                    return 'img2.8comic.com/3/'
                return 'img2.8comic.com/4/'

        html_string = str(code(manga_index, chapter_index))
        pic_start_index = int(html.find(html_string))
        pic_end_index = pic_start_index + len(html_string) + len(str(manga_index)) + 1 + len(str(chapter_index)) + 12
        pic_url = 'http://' + html[pic_start_index:pic_end_index]
        print(pic_url)
      
        f = open('{}/{}/{}_{}.jpg'.format(folder, chapter_index, chapter_index, str(count)), 'wb')
        f.write(urllib.request.urlopen(pic_url).read())
        f.close()
        
        return html, driver


while True:  
    print('選擇要下載的漫畫 (Please select the option you like)')
    print('1. 航海王(One Piece)')
    print('2. 火影忍者 (Naruto)')
    print('3. 一拳超人 (One Punch Man)')
    print('4. 離開 (Exit)')
    print('請輸入編號(Please enter your option)：')
    answer = input()
    if answer == '1':
        manga_index = '103'
        folder = 'one_piece'
        break
    elif answer == '2':
        manga_index = '102'
        folder = 'naruto'
        break
    elif answer == '3':
        manga_index = '10406'
        folder = 'one_punch_man'
        break
    elif answer == '4':
        print('Bye-Bye!')
        sys.exit()
    else:
        print('不要調皮 (Please enter 1-4)\n')

print("請輸入第幾話(Please enter the chapter you like): ")
chapter_index = input()
if os.path.isdir(folder):
    cmd = 'cd '+folder+'; mkdir '+chapter_index+'; cd '+chapter_index
    os.system(cmd)
else:
    os.makedirs(folder)
    cmd = 'cd '+folder+'; mkdir '+chapter_index+'; cd '+chapter_index
    os.system(cmd)
get_manga(manga_index, chapter_index, folder)

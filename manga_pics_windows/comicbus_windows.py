from selenium import webdriver
import time
import urllib.request
import math
import os
import sys

def get_manga(manga_index, chapter_index, folder):
    start = time.time()
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options) #For Windows users
    try:
        url = 'https://www.8899.click/online/comic-' + str(manga_index) + '.html?ch=' + str(chapter_index)
        driver.get(url)
        count = 1
        html, driver = Pics.get_pics(manga_index, chapter_index, url, driver, count)

        page_start_index = int(html.find('第1/')) + 3
        page_end_index = int(html.find('頁</font>'))
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
        print('咦 有地方出錯了 請再次確認你的輸入')
        print('(Hmm... There is something wrong. Please make sure you enter correctly.)')
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

        search_str = '<img name="TheImg" border="0" id="TheImg" src="//'
        pic_url_start_index = int(html.find(search_str)) + len(search_str)
        pic_url_end_index = pic_url_start_index + 18 # 18 is the length of "img3.8comic.com/2/"" part
        pic_url_root = html[pic_url_start_index: pic_url_end_index] 

        html_string = str(pic_url_root)
        pic_start_index = int(html.find(html_string))
        pic_end_index = pic_start_index + len(html_string) + len(str(manga_index)) + 1 + len(str(chapter_index)) + 12
        pic_url = 'http://' + html[pic_start_index:pic_end_index]
        print(pic_url)

        try:
            f = open(r'{}\\{}\\{}_{}.jpg'.format(folder, chapter_index, chapter_index, str(count)), 'wb')
            f.write(urllib.request.urlopen(pic_url).read())
            f.close()
        except:
            f.close()
            os.system('rd /Q /S ' + folder + r'\\' + str(chapter_index)) # Delete the "wrong" file folder
        return html, driver

while True:   
    print('選擇要下載的漫畫 (Please select the option you like)\n')
    print('1. 航海王 (One Piece)')
    print('2. 火影忍者 (Naruto)')
    print('3. 一拳超人 (One Punch Man)')
    print('4. 七原罪 (七つの大罪)')
    print('5. 銀魂 (Gintama)')
    print('6. 獵人 (Hunter x Hunter)')
    print('7. 離開 (Exit)\n')
    print('< by Raymond Yang Sep. 2019 >')  
    print('請輸入編號 (Please enter your option)：')
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
        manga_index = '9418'
        folder = 'seven_deadly_sins'
        break
    elif answer == '5':
        manga_index = '1551'
        folder = 'gintama'
        break
    elif answer == '6':
        manga_index = '105'
        folder = 'hunter'
        break
    elif answer == '7':
        print('Bye-Bye!')
        sys.exit()
    else:
        print('不要調皮 (Please enter 1-6)\n')

print('請輸入第幾話 (Please enter the chapter you like): ')
chapter_index = input()
# print(os.getcwd())
if os.path.isdir(folder):
    os.system('cd '+folder)
    os.system('mkdir '+ folder+ r'\\' + chapter_index)
    os.system('cd '+ folder+ r'\\' + chapter_index)
else:
    os.makedirs(folder)
    os.system('cd '+folder)
    os.system('mkdir '+ folder+ r'\\' + chapter_index)
    os.system('cd '+ folder+ r'\\' + chapter_index)
try:
    get_manga(manga_index, chapter_index, folder)
except:
    print(' -- 強制終止 (The process has been terminated.) --')

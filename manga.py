from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import urllib
import math


def get_pics(manga_index, chapter_index):
    start = time.time()
    try:
	    url = 'https://www.8899.click/online/comic-' + str(manga_index) + '.html?ch=' + str(chapter_index)

	    driver = webdriver.Chrome(ChromeDriverManager().install())  # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
	    driver.get(url)

	    def tryclick(driver, selector, count=0):  ##保護機制，以防無法定味道還沒渲染出來的元素
	        try:
	            elem = driver.find_element_by_css_selector(selector)
	            # elem = driver.find_element_by_xpath(Xpath)  # 如果你想透過Xpath定位元素
	            elem.click()  # 點擊定位到的元素
	        except:
	            # time.sleep(2)
	            count += 1
	            if (count < 2):
	                tryclick(driver, selector, count)
	            # else:
	            #     print("cannot locate element" + selector)

	    tryclick(driver, "#flang > option:nth-child(2)")  # 設定成中文
	    tryclick(driver, "#crstime_search")  # 點擊「檢索」按鍵
	    # time.sleep(3) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
	    html = driver.page_source  # 取得html文字

	    # print(html) # Show the page source
	    page_start_index = int(html.find('第1/')) + 3
	    page_end_index = page_start_index + 2
	    total_page_num = int(html[page_start_index:page_end_index])  # Received the total pages of this chapter

	    # Find the pic and download it
	    pic_start_index = int(html.find('img3.8comic.com/2/'))
	    pic_end_index = pic_start_index + len('img3.8comic.com/2/') + len(str(manga_index)) + 1 + len(
	        str(chapter_index)) + 12
	    pic_url = 'http://' + html[pic_start_index:pic_end_index]
	    print(pic_url)

	    count = 1
	    f = open('{}_{}.jpg'.format(chapter_index, str(count)), 'wb')
	    f.write(urllib.request.urlopen(pic_url).read())
	    f.close()
	    count += 1

	    url_list = []
	    for i in range(2, total_page_num + 1):
	        url_ext = url + '-' + str(i)
	        url_list.append(url_ext)

	    for url in url_list:
	        driver.get(url)
	        tryclick(driver, "#flang > option:nth-child(2)")  # 設定成中文
	        tryclick(driver, "#crstime_search")  # 點擊「檢索」按鍵
	        # time.sleep(3) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
	        html = driver.page_source  # 取得html文字
	        pic_start_index = int(html.find('img3.8comic.com/2/'))
	        pic_end_index = pic_start_index + len('img3.8comic.com/2/') + len(str(manga_index)) + 1 + len(
	            str(chapter_index)) + 12
	        pic_url = 'http://' + html[pic_start_index:pic_end_index]
	        print(pic_url)
	        f = open('{}_{}.jpg'.format(chapter_index, str(count)), 'wb')
	        f.write(urllib.request.urlopen(pic_url).read())
	        f.close()
	        count += 1

	    driver.close()  # 關掉Driver打開的瀏覽器
	    end = time.time()
	    second = math.floor((end - start) % 60)
	    minute = math.floor((end - start - second) / 60)
	    avg = round((end - start) / total_page_num, 3)
	    print('Finished')
	    print('Total time:', minute, 'm', second, 's')
	    print('Avg. time:', avg, 's')
    except:
        print('Incorrect index entered. 幹 有錯喔')
        driver.close()
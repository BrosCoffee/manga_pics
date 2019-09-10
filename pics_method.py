import urllib

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
        pic_start_index = int(html.find('img3.8comic.com/2/'))
        pic_end_index = pic_start_index + len('img3.8comic.com/2/') + len(str(manga_index)) + 1 + len(str(chapter_index)) + 12
        pic_url = 'http://' + html[pic_start_index:pic_end_index]
        print(pic_url)
      
        f = open('{}_{}.jpg'.format(chapter_index, str(count)), 'wb')
        f.write(urllib.request.urlopen(pic_url).read())
        f.close()
        
        return html, driver
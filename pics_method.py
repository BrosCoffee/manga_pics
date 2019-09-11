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
      
        f = open('{}_{}.jpg'.format(chapter_index, str(count)), 'wb')
        f.write(urllib.request.urlopen(pic_url).read())
        f.close()
        
        return html, driver
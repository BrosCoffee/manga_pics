# Introduction:

The project was inspired by my younger brother, Randy. Five days ago, he showed me an app that allows users to download pics 
from Instagram. The instructions are very simple: users enter the Instagram account and the number of pics they like.
The folder named after the account will be created, and then the pics will be downloaded and be stored in the folder. 

It got me interested cuz I knew the concepts of how to make it and I had also created something similar in the past when 
I was studyinh at the III. The one I created was not as good as the Instagram app, so I wanna challenge myself and 
created one with clean and OOP style codes (see comicbus.py file). Also I wanna make this project fun and useful. Randy 
gave me some ideas: because he is a big fan of the Japanese manga "One Piece", he visits website: 
https://www.comicbus.com on the weekly basis. What bothers him is that 
his company's dorm has bad wifi connections, it usually takes him forever to read a chapter online. So after the 
discussing about his needs, I decided to create an app that allows users to customize and download the manga they like. 
###### (The manga are all in traditional Chinese characters, it might be inconvenient for the pure English readers.)
# Instruction:
### comicbus_windows2.1.exe 

 * The purpose of this project is for personal hobby and academic research. PLEASE DO NOT distribute this project due to
  the potential infringement of the copyright. Thank you for your cooperation.
  
 * The app has six manga to choose at this moment: One Piece, Naruto, One Punch Man, Seven Deadly Sins, Gintama, and 
 Hunter x Hunter. The category is extendable, and it only takes a few minutes for a new extension.
 
 * The following instructions is for the "comicbus_windows2.1.exe" app which only works under the Windows system.

1. Prerequisite:
    * Google Chrome browser version 77.x and up
    * Select the "three-dot" button on the upper right corner -> 說明(E) -> About Google Chrome(G)
    * The browser will be auto-upgraded. Close and open again, it will be the newest version.
2. Be awared, the "chromedriver.exe" and the "comicbus_windows2.1.exe" apps must be in the same folder.
3. Double-click the "comicbus_windows.exe" app.
4. Select the manga you like.
5. Select whether to download one or multiple chapters/ episodes.**
6. The Windows firewall will prompt and ask "allow access" for the app (virus-free guarantee, cuz I dunno how to make
 one yet, lol)
7. The managa you selected will be download the the file folder.

** Because the app was written based on the website: https://www.comicbus.com/ , users must be awared the input they
entered. Some categories of manga are constructed all by "chapters", the others are by the mixed of "episodes" and 
"chapters"; some manga are finished, and the others are still to be continued. In general, each chapter has 15-20 pages,
and an episode has 100+ pages. Be very careful when you select your options. The following part is each category's 
details as on today (Sep. 14th 2019):

1. One Piece: 1-68(Episode) 471-955~(Chapter) (It will shows error messages if the chapter or episode doesn't exist.
 ex: Chapter 121 in One Piece)
2. Naruto: 1-58(Episode) 370-710~(Chapter)
3. One Punch Man: 1-158~(Chapter)
4. Seven Deadly Sins (七つの大罪): 1-325~(Chapter)
5. Gintama: 1-40(Episode) 167-704~(Chapter)
6. Hunter x Hunter: 1-32(Episode) 261-390~(Chapter)

Raymond Yang (Sep. 14th 2019)

# 使用指南:
<純屬學術研究用，請勿轉載>

### comicbus_windows2.1.exe

這支程式是使用python3.7 和 selenium 所寫的爬蟲，爬取的是https://www.comicbus.com/ 這個網站
以下是這支程式的使用說明(+附錄)

1. 環境需求(Prerequisite):
    Google Chrome 瀏覽器 77.x 以上版本
    選擇 瀏覽器右上角三個點的按鈕 -> 說明(E) -> 關於Google Chrome(G)
    瀏覽器會自動更新，更新完關掉重開就是最新的版本
2. 注意，"chromedriver.exe" 這個執行檔必須和"comicbus_windows.exe" 在同個檔案夾
3. 選擇 "comicbus_windows.exe" 這個檔案
4. 輸入喜歡的漫畫
5. 選擇下載單話(集)或是多話(集)**附錄1 
6. 防火牆會問給不給過(放心絕對沒病毒，因為我還不會寫病毒~)
7. 你喜歡的漫畫就會被下載到檔案夾了

附錄1:
	因為是根據https://www.comicbus.com/ 這個網站寫的，所以在輸入"第幾話"時就要注意
有的漫畫全部都是"第幾話"，而有的是"第幾話"和"第幾集"混搭; 有些漫畫完結了，有些還在連載。
一般來說，每一話差不多15-20頁，而每一集可高達100+頁，所以選擇下載時需要注意。
以下是根據今天(Sep. 14th 2019) 每部漫畫的細節:
1. 航海王 (One Piece): 1-68(集) 471-955~(話) (如果輸入沒有的數字就會報錯 ex: 121話)
2. 火影忍者 (Naruto): 1-58(集) 370-710~(話)
3. 一拳超人(One Punch Man): 1-158~(話)
4. 七原罪 (七つの大罪): 1-325~(話)
5. 銀魂 (Gintama): 1-40(集) 167-704~(話)
6. 獵人 (Hunter x Hunter): 1-32(集) 261-390~(話)

Raymond Yang (Sep. 14th 2019) 

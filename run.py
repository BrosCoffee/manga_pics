import manga
import sys

# print('1. 航海王 (One Piece): 103')
# print('2. 火影忍者 (Naruto): 102')
# print('3. 一拳超人 (One Punch Man) 10406')
# print('請輸入漫畫代號(Please enter code)： ')
# print('請輸入第幾話(Enter the chapter you like.)： ')
def main():
	manga_index = sys.argv[1]	
	chapter_index = sys.argv[2]
	manga.get_pics(manga_index, chapter_index)

if __name__ == '__main__':
	main()

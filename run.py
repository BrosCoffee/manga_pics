import manga
import sys

def main():
	manga_index = sys.argv[1]	
	chapter_index = sys.argv[2]
	manga.get_manga(manga_index, chapter_index)

if __name__ == '__main__':
	main()

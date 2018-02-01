from sys import argv
import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
import os
from datetime import datetime as dt

def ShowHelp():
	print ('Insta Image Downloader')
	print ('')
	print ('Usage:')
	print ('insta.py [OPTION] [URL]')
	print ('')
	print ('Options:')
	print ('-u [Instagram URL]\tDownload single photo from Instagram URL')
	print ('-f [File path]\t\tDownload Instagram photo(s) using file list')
	print ('-h, --help\t\tShow this help message')
	print ('')
	print ('Example:')
	print ('python insta.py -u https://instagram.com/p/xxxxx')
	print ('python insta.py -f /home/username/filelist.txt')
	print ('')
	exit()

def DownloadSingleFile(fileURL):
	print ('Downloading image...')
	f = urllib.request.urlopen(fileURL)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	metaTag = soup.find_all('meta', {'property':'og:image'})
	imgURL = metaTag[0]['content']
	fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
	urllib.request.urlretrieve(imgURL, 'fileName.jpg')
	
	date_and_time = str(dt.now()).replace(":", "_").replace(" ", "_")
	new_file = date_and_time + ".jpg"
	old_file = "fileName.jpg"

	try:
		os.rename(old_file, new_file)
		print("File name is: " + new_file)
	except FileNotFoundError:
		print("The file name is already changed")


if __name__ == '__main__':
	if len(argv) == 1:
		ShowHelp()

	if argv[1] in ('-h', '--help'):
		ShowHelp()
	
	elif argv[1] == '-u':
		instagramURL = argv[2]
		DownloadSingleFile(instagramURL)

	elif argv[1] == '-f':
		filePath = argv[2]
		f = open(filePath)
		line = f.readline()
		while line:
			instagramURL = line.rstrip('\n')
			DownloadSingleFile(instagramURL)
			
			line = f.readline()
		f.close()

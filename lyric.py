#-------------------------------------------------------------------------------------------------
#Name :Lyrics Downloader
#Author : Vijetha PV
#Description :Just double click on the lyric.py , enter the name and artist of the song
#and automatically saves the lyrics in the file you specify
#Requirement Python 2.7.x download from "http://python.org/download/"
# You also need to install BeautifulSoup "http://www.crummy.com/software/BeautifulSoup/#Download"
# using either pip or easy_install or manual download
#
#-------------------------------------------------------------------------------------------------
import urllib
import re
import sys,os,inspect
from BeautifulSoup import BeautifulSoup
s=raw_input("Enter the correct name of the song:  ").strip(" ").lower()

artist=raw_input("Enter the correct name of the artist:  ").strip(" ").lower()

s =s.replace(" ","")
artist= artist.replace(" ","")
url='http://www.azlyrics.com/lyrics/'+artist+'/'+ s+'.html'
htmltext = urllib.urlopen(url).read()
soup =BeautifulSoup(htmltext)
products= soup.findAll("div", style = "margin-left:10px;margin-right:10px;")
lyrics= " ".join(str(x) for x in products)
takeoff=['<br />','</div>','<i>','</i>','<div style="margin-left:10px;margin-right:10px;">']
for j in takeoff:
    lyrics=lyrics.replace(j,"\n")
print lyrics
#change the argument inside os.chdir so that you can store all of your lyrics in that directory
# example os.chdir("c:/users/yourusename/YourLyricsFolder/")
os.chdir("C:/Users/vijay/Music/lyrics/")
with open (s+".txt","wb") as l:
    l.write(lyrics)
l.close()





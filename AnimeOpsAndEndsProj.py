# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:13:00 2020

@author: markm
"""

import requests
import urllib.request
import urllib.parse
import re

  
  
userN = str(input("Enter in your MAL username. No speces or other characters please: "))
url = "https://myanimelist.net/animelist/" + userN + "?status=2"
webResponse = requests.get(url)
htmlStr = webResponse.text
search = "anime_title"
index = [m.start() for m in re.finditer(search, htmlStr)]
animeTitles = []
for i in index:
    start = i+24
    end = (htmlStr.find('&', start))
    animeTitles.append(htmlStr[start:end])
animeTitles.pop(-1)
print(animeTitles)


#partial help from Grant Curell's page on how to search for youtube videos
n = 0
for i in animeTitles:
    query_string = urllib.parse.urlencode({"search_query" : animeTitles[n] + " all openings and endings"}) 
    #this is the problem, html_content returns something not right.
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])
    n+=1





#matches = re.finditer("anime_title", anime_titles[0])

##for link in soup.find_all('a'):
##   print(link.get('href'))

# To download the whole data set, let's do a for loop through all a tags
##line_count = 1 #variable to track what line you are on
##for one_a_tag in soup.findAll('a'):  #'a' tags are for links
##    if line_count >= 36: #code for text files starts at line 36
##        link = one_a_tag['href']
##        download_url = 'https://myanimelist.net/animelist/" + userN + "?status=2'+ link
##        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
##        time.sleep(1) #pause the code for a sec
    #add 1 for next line
##    line_count +=1


# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:13:00 2020

@author: markm
"""

import requests
import urllib.request
import urllib.parse
import re

  
cont = False
while cont == False:
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
    if(len(animeTitles) == 0):
        print("\nUsername not found! Please try again :)")
        continue
    else:
        animeTitles.pop(-1)
        cont = True


print("\nGenerating File...")
file = open("anime_openings.txt", "w")
file.write("Openings for " + userN+"'s finished anime list\n\n")
#Grant Curell's page on how to search for youtube videos with python used for partial reference
n = 0
while n < len(animeTitles):
    query_string = "search_query=" + animeTitles[n].replace(" ", "+") + "+all+openings" 
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    #use regular expression
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    file.write(animeTitles[n] + ":  " + "http://www.youtube.com/watch?v=" + search_results[0])
    file.write("\n")
    print("...")
    n+=1

file.close()
print("Done! File has been created, and contains the openings to all of your finished anime! File is named anime_openings.txt. Enjoy!")
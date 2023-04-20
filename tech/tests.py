from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
# Create your views here.
key = 'https://www.numerade.com/questions/bulletbullet-a-mass-spring-system-is-in-shm-in-the-horizontal-direction-if-the-mass-is-025-mathrmkg-/'
headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
 }
page = requests.get(key, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
lists = soup.findAll('script')
listt = soup.findAll('track')
print(listt)
listt = str(listt)
listt = listt.split(" ")
print(listt)
if 'kind="captions"' in listt:
    print(True)
    listt = str(listt)
    index = listt.find("captions/")
    start_index = index+9
    end_index = start_index+36
    url = listt[start_index:end_index]
    print(url)
    result = 'https://cdn.numerade.com/encoded/{}.mp4'.format(url)
    print(result)
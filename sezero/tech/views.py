from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request,"sezero_tech.html")

def test(request):
    tes=''
    try:
        if request.method=="POST":
            data = request.POST.get('data')
            tes = data+"python"+"anywhere"
    except:
        tes="yoi bro"
    
    return render(request,"index.html",{'tes':tes})

def scrape(request):
    data = []
    if request.method == 'POST':
        key = request.POST.get('q-url')
        headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        page = requests.get(key, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        lists = soup.findAll('script')
        for list in lists:
            if 'videoUrl' in list.text:
                videoUrl = list.text.strip()
                index = videoUrl.find("videoUrl")
                start_index = index+12
                end_index = start_index+36
                videoUrl = videoUrl[start_index:end_index]

                result = 'https://cdn.numerade.com/encoded/{}.mp4'.format(videoUrl)
                result = requests.get(result,headers=headers)
                if result.status_code == 200:
                    result = 'https://cdn.numerade.com/encoded/{}.mp4'.format(videoUrl)
                    data.append(result)
                    
                else:
                    result = 'https://cdn.numerade.com/ask_video/{}.mp4'.format(videoUrl)
                    data.append(result)
    data = ''.join(data)
    data = str(data)
    
    return render(request,"scrape.html", {"data":data})

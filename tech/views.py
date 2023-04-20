from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request,"sezero_tech.html")
def home_scrape(request):
    return render(request,"home_scrape.html")
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
    else:
        error = 'fill the url correctly!'
    data = ''.join(data)
    data = str(data)
    
    return render(request,"scrape.html", {"data":data},{"error":error})

from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib import messages
from django.forms import ModelForm, TextInput
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','body']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Your Title'}),
            'body': TextInput(attrs={'placeholder': 'Your Title'}),
        }
        labels = {
            'title': '',
            'body': '',
        }
def landing(request):
    return render(request, 'home.html')
def projects(request):
    return render(request, 'projects.html')
def blog_home(request):
    return render(request, 'blog_home.html')
def home(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            messages.success(request,'submitted succesfully {}'.format(post))
            return redirect('/')      
    form=PostForm()
    return render(request,'index.html',{'form':form})

def editpost(request,title):
    instance = get_object_or_404(Post, title=title)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/blog/{}/'.format(instance.title))
    return render(request, 'edit.html', {'form': form})

def postdetail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'detail.html',{'post':post})


@requires_csrf_token
def uploadi(request):
    f=request.FILES['image']
    fs=FileSystemStorage()
    filename=str(f).split('.')[0]
    file= fs.save(filename,f)
    fileurl=fs.url(file)
    return JsonResponse({'success':1,'file':{'url':fileurl}})

@requires_csrf_token
def uploadf(request):
        f=request.FILES['file']
        fs=FileSystemStorage()
        filename,ext=str(f).split('.')
        print(filename,ext)
        file=fs.save(str(f),f)
        fileurl=fs.url(file)
        fileSize=fs.size(file)
        return JsonResponse({'success':1,'file':{'url':fileurl,'name':str(f),'size':fileSize}})


def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup  

    print(request.GET['url'])
    url = request.GET['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text,features="html.parser")
    metas = soup.find_all('meta')
    description=""
    title=""
    image=""
    for meta in metas:
        if 'property' in meta.attrs:
            if (meta.attrs['property']=='og:image'):
                image=meta.attrs['content']         
        elif 'name' in meta.attrs:         
            if (meta.attrs['name']=='description'):
                description=meta.attrs['content']
            if (meta.attrs['name']=='title'):
                title=meta.attrs['content']
    return JsonResponse({'success':1,'meta':
    {"description":description,"title":title, "image":{"url":image}
        }})
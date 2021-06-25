from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .forms import *
def index(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request,'index.html',context)
def new_by_id(request,id):
    new = News.objects.get(id=id)
    print(new.text)
    context = {
        'new':new
    }
    return render(request,'one_new.html',context)
def about(request):
    return HttpResponse('Biz haqimizda..')

def politics(request):
    news = News.objects.filter(tag='siyosat')
    context = {
        'news':news
    }
    return render(request,'index.html',context)

def by_tag(request,tag):
    news = News.objects.filter(tag=tag)
    context = {
        'news':news
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse('Biz haqimizda..')

def add_news(request):
    form = AddNews()
    theme = request.POST.get('theme')
    text = request.POST.get('text')
    tag = request.POST.get('tag')
    image = request.POST.get('image')
    form = AddNews(request.POST,request.FILES)

    if form.is_valid():
        print('is valid...')
        new = News(theme=theme,text=text,tag=tag,image=image)
        new.save()
    context = {
        'form':form
    }
    return render(request,'add_news.html',context)
def post_news(request):
    form = PostNews()
    form = PostNews(request.POST,request.FILES)
    if form.is_valid():
        print('is valid...')
        form.save()
    context = {
        'form':form
    }
    return render(request,'add_news.html',context)

def contact(request):
    return HttpResponse('Biz bilan aloqa..')
def messages(request):
    return HttpResponse('Xabarlar..')
def regestrationView(request):
    form = ProfileForm(request.POST)
    print(request.POST)
    if form.is_valid():
        print('is valid .. ')
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request=request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
    context = {
        'form':form
    }
    return render(request,'regestration.html',context)
def log_in(request):
    form = LoginForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request,username=username,password=password)
    if user:
        login(request,user)
        return redirect('index')
    context = {
        'form':form
    }
    return render(request,'login.html',context)
def log_out(request):
    user=request.user
    if user:
        logout(request)
    return redirect('login')

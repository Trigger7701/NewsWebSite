from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import News
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .forms import *
from .decorator import *
def index(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request,'index.html',context)
def new_by_id(request,id):
    new = News.objects.get(id=id)
    comments = Comment.objects.filter(new=new)
    form = CommentForm()
    if request.POST:
        profile = Profile.objects.get(user = request.user)
        form = CommentForm(request.POST)
        if form.is_valid():
            text = request.POST.get('text')
            print(text)
            comment = Comment.objects.create(new=new, user=profile, text=text)
            comment.save()
    context = {
        'form':form,
        'new':new,
        'comments':comments
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
@login_required(login_url='login')
@allowed_users(allowed=['admins,editors'])
def by_tag(request,tag):
    news = News.objects.filter(tag=tag)
    context = {
        'news':news
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse('Biz haqimizda..')
@login_required(login_url='login')
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
# @login_required(login_url='login')
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
            profile = Profile.objects.create(user = user)
            profile.save()
            login(request,user)
            return redirect('index')
    context = {
        'form':form
    }
    return render(request,'regestration.html',context)
@authenticated
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
def like_dislike(request):
    print(request.POST)
    return JsonResponse({'status':'ishladi..'})

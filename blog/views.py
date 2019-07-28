from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all().order_by('-id') # 객체 묶음 가져오기
    return render(request, 'blog/home.html', {'blogs':blogs})

def detail(request, blog_id) : 
    blog_detail = get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog() # 객체 틀 하나 가져오기
    blog.title = request.GET['title']  # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 객체 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

def edit(request,blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'blog/edit.html', {'blog':blog})

def update(request,blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.title = request.GET['title'] # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    blog= get_object_or_404 (Blog, pk=blog_id)
    blog.delete()
    return redirect('home')
from django.contrib.auth import authenticate, logout
from django.shortcuts import render , redirect
from .form import *
# Create your views here.


def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'loginpage.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    return render(request, 'registerpage.html')

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
        return render(request, 'blog_detail.html', context)
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html' )

def see_blog(request):
    context = {}
    try:
        all_blogs = BlogModel.objects.filter(user = request.user)
        context['all_blogs'] = all_blogs
        return render(request, 'see_blog.html', context)
    except Exception as e:
        print(e)
    
    return render(request, 'see_blog.html')


def delete_blog(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if request.user == blog_obj.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see_blog/')

def update_blog(request, slug):
    context = {}
    try:
        updt_blog = BlogModel.objects.filter(slug = slug).first()

        if request.user != updt_blog.user:
            redirect('/')

        initial_dict = {'content':updt_blog.content}
        form = BlogForm(initial=initial_dict)
        
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            
            updt_blog.content = content
            updt_blog.title = title
            updt_blog.image = image
            updt_blog.save()

        context['blog'] = updt_blog
        context['form'] = form

    except Exception as e:
        print(e)
    
    return render(request, 'update_blog.html', context)

def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            return redirect('/add_blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)


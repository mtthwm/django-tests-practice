from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from homepage.models import BlogPost
from homepage.forms import UserForm
from django.contrib.auth import authenticate, login
User = get_user_model()

# Create your views here.
class BlogView(View):
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(BlogPost, pk=kwargs.get('blog_pk'), published=True)
        return render(request, 'homepage/blog.html', context={'blog': blog})

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = BlogPost.objects.published()
        context = {
            'blogs': blogs,
        }
        return render(request, 'homepage/blogs.html', context=context)
    
class UserView(View):
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            u = User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            u.save()
            login(u)
        else:
            print(form.errors)

class AboutView(View):
    def get (self, request, *args, **kwargs):
        return render(request, 'homepage/about.html', context={})

class ResumeView(View):
    def get (self, request, *args, **kwargs):
        return render(request, 'homepage/resume.html', context={})

def loginView (request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.get(username=username)
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
    else:
        context = {
            'form': UserForm(),
        }
        return render(request, 'homepage/login.html', context)
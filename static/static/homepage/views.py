from django.shortcuts import render
from django.views import View
from homepage.forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'homepage/index.html', context={})

class UserView(View):
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            u = User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            u.save()
            login(u)
        else:
            print(form.errors)

def loginView (request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.get(username=username)
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, user)
    else:
        context = {
            'form': UserForm(),
        }
        return render(request, 'homepage/login.html', context)
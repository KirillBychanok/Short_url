import pyshorteners
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import GoodUrl
from .models import CollectUrl


def index(request):
    return render(request, 'main/index.html',)


class NewPerson(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'main/signup.html'


class NewPersonLogin(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'main/login.html'


class NewPersonLogout(LogoutView):
    template_name = 'main/index.html'


@login_required
def checkurl(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bbf = GoodUrl(request.POST)
            if bbf.is_valid():
                short_url = pyshorteners.Shortener().tinyurl.short(bbf.cleaned_data.get('url'))
                CollectUrl.objects.create(url=bbf.cleaned_data.get('url'), short_url=short_url, user=request.user)
                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                context = {'form': bbf}
                return render(request, 'main/create.html', context)
        else:
            bbf = GoodUrl()
            context = {'form': bbf}
            return render(request, 'main/create.html', context)


@login_required
def allurls(request):
    if request.user.is_authenticated:
        all_list = CollectUrl.objects.filter(user=request.user)
        context = {'list': all_list}
        return render(request, 'main/listurls.html', context)

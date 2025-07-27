from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from users.models import user


# Create your views here.

class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('blog:post-list'))
        return render(request, 'users/register.html', {'form': form})
    
class LoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('blog:post-list'))
        return render(request, 'users/login.html', {'form': form})
    
class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')
    
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('blog:post-list'))
    
class UserProfileView(generic.DetailView):
    model = user
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(user, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.post_set.all()
        return context
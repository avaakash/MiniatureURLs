from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from core.models import StoredUrls


def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    context['form'] = form
    return render(request, 'accounts/register.html', context)


@login_required
def dashboard(request):
    urls = StoredUrls.objects.filter(user=request.user).order_by('-creation_time')
    return render(request, 'dashboard.html', context={'urls': urls})

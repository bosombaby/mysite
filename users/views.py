from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

    form = NewUserForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def profile_add(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user, image=image, contact_number=contact_number)
        profile.save()
        print(contact_number, user, image)
    return render(request, 'users/profile_add.html')


def profile_seller(request, id):
    seller = User.objects.get(id=id)
    context = {'seller': seller}
    return render(request, 'users/profile_seller.html', context)

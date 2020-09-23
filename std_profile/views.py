from django.shortcuts import render, redirect
from .models import Profile



def profiles(request):
    Profile_list = Profile.objects.all()

    return render(request,'profile.html',{'Profile_list':Profile_list},)


def details(request):

    profile = Profile.objects.all()

    return render(request, 'detail.html', {'profile':profile},)




from django.shortcuts import render
from .models import Fav, Logo, HomeBgInfo, About, Project, Gallery
# Create your views here.

def index(request):
    fav_icon = Fav.objects.first()
    home_logo = Logo.objects.first()
    home_bg_info = HomeBgInfo.objects.first()
    about = About.objects.first()
    projects = Project.objects.all()
    gallery_list = Gallery.objects.all()
    return render(request, 'main/index.html', context={
        'fav_icon': fav_icon,
        'home_logo':home_logo,
        'home_bg_info':home_bg_info,
        'about':about ,
        'gallery_list':gallery_list,
        'projects':projects
    })
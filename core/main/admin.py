from django.contrib import admin
from .models import Logo, HomeBgInfo, Fav, About, Project, Gallery
# Register your models here.

admin.site.register(Fav)
admin.site.register(Logo)
admin.site.register(HomeBgInfo)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Gallery)
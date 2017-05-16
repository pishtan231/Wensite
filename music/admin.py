from django.contrib import admin
from .models import Album, Song
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Album)
admin.site.register(Song)
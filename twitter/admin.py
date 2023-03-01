from django.contrib import admin
from .models import Profile,Tweet,Comment,Followers

admin.site.register(Profile)
admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Followers)
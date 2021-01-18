from django.contrib import admin
from wall_app.models import Post, User, Comment
# Register your models here.

admin.site.register([Post, User, Comment])
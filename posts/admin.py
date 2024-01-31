from django.contrib import admin
from .models import Post,Like,DisLike
# Register your models here.
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(DisLike)
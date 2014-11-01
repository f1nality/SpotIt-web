from django.contrib import admin
from core.models import User
from spotit.models import PostComment, Post

admin.site.register(Post)
admin.site.register(PostComment)

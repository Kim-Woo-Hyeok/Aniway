from django.contrib import admin

from .models import Question
from .models import Blog

admin.site.register(Question)
admin.site.register(Blog)
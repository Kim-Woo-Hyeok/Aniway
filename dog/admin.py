from django.contrib import admin

from .models import Mission
from .models import Community
from .models import Life

admin.site.register(Mission)
admin.site.register(Community)
admin.site.register(Life)
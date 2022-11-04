from django.contrib import admin

from .models import Mission, Mission_detail
from .models import Community
from .models import Life, Life_detail
from .models import SaveIp
from .models import Pack, Pack_detail

admin.site.register(Mission)
admin.site.register(SaveIp)
admin.site.register(Community)
admin.site.register(Life_detail)
admin.site.register(Life)
admin.site.register(Pack)
admin.site.register(Pack_detail)
admin.site.register(Mission_detail)
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/', include('card.urls')),
    path('polls/', include('polls.urls')),
    path('homepage/', include('homepage.urls')),
    path('dog/', include('dog.urls')),
    # 추가하지 않으면 login 페이지에 접근할 수 없다.
    path('card/', include('django.contrib.auth.urls')),
    path('dog/', include('django.contrib.auth.urls')),
    path('homepage/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
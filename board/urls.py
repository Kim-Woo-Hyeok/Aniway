from django.urls import path
from . import views
# from .views import Main
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    #  path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    #  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
     path('post/main/', views.home, name='post_main'),
     path('post/test/', views.test, name='post_test'),
     # path('card/', views.card, name='card'),
    # path('lecture/', views.post_lecture, name='post_lecture'),
    # path('', Main.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
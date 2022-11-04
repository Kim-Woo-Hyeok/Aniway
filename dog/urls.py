from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dog'

urlpatterns = [
    path('signup_page/', views.signup_page, name='signup_page'),
    path("test/", views.test, name="test"),
    path('base/', views.base, name='base'),
    path('mission_detail/', views.mission_detail, name='mission_detail'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('dog_main/', views.dog_main, name='dog_main'),
    path('signup_pet/', views.signup_pet, name='signup_pet'),
    path('mission_list/', views.mission_list, name='mission_list'),
    path('mission_edu/', views.mission_edu, name='mission_edu'),
    path('company/', views.company, name='company'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('finish/', views.finish, name='finish'),
    path('community/', views.community, name='community'),
    path('need_edu/', views.need_edu, name='need_edu'),
    path('mypage/', views.mypage, name='mypage'),
    path('package/', views.package, name='package'),
    path('life_detail/', views.life_detail, name='life_detail'),
    path('pack_detail/', views.pack_detail, name='pack_detail'),
    path('life_edu/', views.life_edu, name='life_edu'),
    path('misson_choice/', views.misson_choice, name='misson_choice'),
    path('community_click/', views.community_click, name='community_click'),
    path('mission_page_list/', views.mission_page_list, name='mission_page_list'),
    path('community_click/<int:pk>', views.posting, name="posting"),
    path('life_detail/<int:pk>', views.life_ip, name="life_ip"),
    path('mission_detail/<int:pk>', views.mission_ip, name="mission_ip"),
    path('pack_detail/<int:pk>', views.pack_ip, name="pack_ip"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

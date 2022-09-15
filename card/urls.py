from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'card'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('card/', views.card, name='card'),
    path('main/', views.main, name='main'),
    path('business/', views.business, name='business'),
    path('now/', views.now, name='now'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


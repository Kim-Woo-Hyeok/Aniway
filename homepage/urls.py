from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'homepage'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('homepage/', views.homepage, name='homepage'),
    # path('login/', views.login_page, name='login_page'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name="logout"),
    path('signup/', views.signup, name='signup'),
    path('infopage/', views.infopage, name='infopage'),
    path('infopage_click/', views.infopage_click, name='infopage_click'),
    path('infopage_click/<int:pk>', views.posting, name='posting'),
    path('business/', views.business, name='business'),
    path('service_center/', views.service_center, name='service_center'),
    path('business_network/', views.business_network, name='business_network'),
    path('test/', views.test, name='test'),
 ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
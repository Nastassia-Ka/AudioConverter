from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='home'),
    path('user/', views.user_account, name='user_account'),
    path('login/',views.login, name='login'),
    path('registration', views.user_reg, name='user_reg'),
    path('about/', views.about, name='about'),
    path('deletion/', views.deletion_page, name='deletion page'),
]

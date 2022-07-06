from django.urls import path, re_path
from django.conf.urls.static import static
from .views import *
from AudioConverter import settings

urlpatterns = [
    path('', home_page, name='home'),
    path('user/', user_account, name='user_account'),
    path('about/', about, name='about'),
    path('deletion/', deletion_page, name='deletion page'),

]

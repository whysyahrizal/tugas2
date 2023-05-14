from django.urls import path
from authentication.views import *
from django.conf.urls import include

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', include('authentication.urls')),
    path('logout/', logout, name='logout'),
]

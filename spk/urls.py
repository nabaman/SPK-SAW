
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView,name='login'),
    path('logout',logoutView,name='logout'),
    path('dashboard/',include('nilai.urls'))

]

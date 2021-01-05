from django.contrib import admin
from django.urls import path
from oursite.views import homepage,data,ind,us,phi,chi,jap

urlpatterns = [
    path('',homepage),
    path('data',data),
    path('admin/', admin.site.urls),
    path('ind',ind),
    path('us',us),
    path('phi',phi),
    path('chi',chi),
    path('jap',jap),

]
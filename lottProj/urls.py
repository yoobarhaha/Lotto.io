
from django.contrib import admin
from django.urls import path
import lottoApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lottoApp.views.home,name="home"),
    path('about/',lottoApp.views.about,name="about"),
    path('result/',lottoApp.views.result,name="result"),
]

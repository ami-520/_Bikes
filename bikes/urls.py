"""
URL configuration for bikes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bajaj.views import *
from royal_enfield.views import *
import honda,ktm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bajaj_pulsarN160/', bajaj_pulsarN160,name='bajaj_pulsarN160'),
    path('royal_enfield_hunter_350/',royal_enfield_hunter_350,name='royal_enfield_hunter_350'),
    path('honda/',include('honda.urls')),
    path('ktm/',include('ktm.urls')),
]

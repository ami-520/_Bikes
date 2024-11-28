from honda.views import *
from django.urls import path

urlpatterns=[
    path('honda_cb350/',honda_cb350,name='honda_cb350'),
    path('honda_unicorn/',honda_unicorn,name='honda_unicorn'),
]
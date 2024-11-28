from ktm.views import * 
from django.urls import path

urlpatterns=[
    path('ktm_350_duke/',ktm_350_duke,name='ktm_350_duke'),
    path('ktm_250_duke/',ktm_250_duke,name='ktm_250_duke'),
]
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bajaj_pulsarN160(request):
    return HttpResponse('<h1>bajaj_pulsarN160 has 164cc<h1/>')

def bajaj_pulsar_RS200(request):
    return HttpResponse('<h1>bajaj_pulsar_RS200 has 199cc<h1/>')
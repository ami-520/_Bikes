from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def honda_cb350(request):
    return HttpResponse('<h1>honda_cb350 has 350cc<h1/>')
def honda_unicorn(request):
    return HttpResponse('<h1><marquee>honda_unicorn has 165cc<h1/><marquee/>')


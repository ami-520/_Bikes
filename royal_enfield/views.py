from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def royal_enfield_hunter_350(request):
    return HttpResponse('<h1><marquee>royal_enfield_hunter_350 has 350cc<maequee/><h1/>')

def royal_enfield_continental_GT_650(request):
    return HttpResponse('<h1><marquee>royal_enfield_continental_GT_650 has 650cc<marquee/><h1/>')

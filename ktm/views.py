from django.shortcuts import render

from django.http import HttpResponse
def ktm_350_duke(request):
    return HttpResponse('<h1><marquee>KTM_390_DUKE has 400cc<marquee/><h1/>')

def ktm_250_duke(request):
    return HttpResponse('<h1><marquee>KTM_390_DUKE has 250cc<marquee/><h1/>')
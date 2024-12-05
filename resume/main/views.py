from django.shortcuts import render
from django.http import HttpResponse

def resume_home(request):
    return render(request, 'main/home_page.html')


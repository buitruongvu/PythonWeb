from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.writelines("<h1>Xin Chao</h1>")
    response.write("Day la app home")
    return response

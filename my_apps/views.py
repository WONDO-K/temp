from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # 응답 생성
    response = HttpResponse("Hello, world!")
    return response
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def deposit(request):
	return HttpResponse('<h1>you can deposit amount</h1>') 




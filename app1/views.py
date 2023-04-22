from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def withdraw(request):
	return HttpResponse('<h1>you can  withdraw amount</h1>')

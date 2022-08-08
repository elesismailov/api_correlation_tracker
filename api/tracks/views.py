from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(req):

    return JsonResponse({'msg': 'tracks index'})
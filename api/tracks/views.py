from django.shortcuts import render
from django.http import JsonResponse

from django.views import View

# Create your views here.

def index(req):

    return JsonResponse({'msg': 'tracks index'})


class Index(View):

    def get(self, req):
        
        return JsonResponse({'msg': 'Class based index'})

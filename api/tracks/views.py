from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View

# Create your views here.

class Index(View):

    def get(self, req):
        print(req.method)
        return JsonResponse({'msg': 'Get all tracks.'})

    def post(self, req):
        print(req.method)
        return JsonResponse({'msg': 'Create new track.'})


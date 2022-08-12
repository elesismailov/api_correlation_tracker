from django.http import JsonResponse, HttpResponse
from django.views import View

import json

from .models import Track

# Create your views here.

class Index(View):

    def get(self, req):
        print(req.method)
        return JsonResponse({'msg': 'Get all tracks.'})


    def post(self, req):

        request_body = json.loads(req.body.decode('utf-8'))
        # TODO handle request body errors 400

        track = Track(
                user = req.current_user,
                title = request_body.get('title'),
                description = request_body.get('description', ''),
                color = request_body.get('color', ''),
                )

        # TODO handle error 500
        track.save()

        # TODO refine response
        return HttpResponse('New track has been created', status=201)




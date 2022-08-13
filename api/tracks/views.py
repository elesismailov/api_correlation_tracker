from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize

import json

from .models import Track
from .serializers import TrackSerializer

# Create your views here.

class Index(View):

    def get(self, req):

        # limit = Track.objects.count() or 10
        
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)

        # TODO ? add some additional fields
        return JsonResponse({ 'tracks': serializer.data }, safe=False)


    def post(self, req):

        request_body = json.loads(req.body.decode('utf-8'))
        # TODO handle request body errors 400

        # TODO check whether user has a track of the same title

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




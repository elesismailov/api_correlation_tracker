from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize

import json

from .models import Track, TrackEntry
from .serializers import TrackSerializer

# Create your views here.

class Index(View):

    def get(self, request):

        # limit = Track.objects.count() or 10

        user = request.current_user
        
        tracks = Track.objects.filter(user=user)

        serializer = TrackSerializer(tracks, many=True)

        # TODO ? add some additional fields
        return JsonResponse({ 'tracks': serializer.data }, safe=False)


    def post(self, request):

        request_body = json.loads(request.body.decode('utf-8'))
        # TODO handle request body errors 400

        # TODO check whether user has a track of the same title

        track = Track(
                user = request.current_user,
                title = request_body.get('title'),
                description = request_body.get('description', ''),
                color = request_body.get('color', ''),
                )

        # TODO handle error 500
        track.save()

        # TODO refine response
        return HttpResponse('New track has been created', status=201)



class Entry(View):

    def post(self, request):

        request_body = json.loads(request.body.decode('utf-8'))
        # TODO handle request body errors 400

        track = Track.objects.get(id=request_body["track_id"])
        # TODO handle no track error

        # TODO handle entry if exists, update
        entry = TrackEntry(
                track = track,
                rating = request_body.get('rating'),
                )

        entry.save()

        return JsonResponse({ "entry": entry}, status=201)

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize
from django.utils import timezone

from django.db.utils import IntegrityError

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


class TrackView(View):

    def get(self, request, track_id):

        user = request.current_user

        # TODO handle 404
        track = Track.objects.get(id=track_id, user=user)

        serializer = TrackSerializer(track)

        # TODO ? add some additional fields
        return JsonResponse({ 'track': serializer.data }, safe=False)



class Entry(View):

    # /api/tracks/track_id/entry
    def post(self, request, track_id):

        # TODO handle request body errors 400
        request_body = json.loads(request.body.decode('utf-8'))

        # TODO handle 404
        track = Track.objects.get(id=track_id)

        entry = TrackEntry(
                track = track,
                date = request_body.get('date', timezone.now().date()),
                rating = request_body.get('rating'),
                )
       
        try:
            # CREATE NEW ENTRY
            entry.save()

        except IntegrityError as e:
            # UPDATE ENTRY
            entry = TrackEntry.objects.get(date=entry.date)
            
            entry.rating = request_body.get('rating')

            entry.save()

        except e:
            raise e

        # TODO implement serializer
        return JsonResponse({}, status=201)
        # return JsonResponse({ "entry": entry}, status=201)





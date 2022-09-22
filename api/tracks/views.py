from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize
from django.utils import timezone

from django.db.utils import IntegrityError

import json
from json.decoder import JSONDecodeError

from .models import Track, TrackEntry
from .serializers import TrackSerializer, TrackEntrySerializer
from api.response_error_handler import ResponseError

from api.tracks.operators import *
from api.tracks.exceptions import *

# Create your views here.

class Index(View):

    # List user tracks 
    def get(self, request):

        user = request.current_user
        
        try:
            tracks = getTracks(user=user)
        except Exception:
            raise Exception

        serializer = TrackSerializer(tracks, many=True)

        # TODO ? add some additional fields
        return JsonResponse({ 'tracks': serializer.data }, safe=False)


    # CREATE NEW TRACK
    def post(self, request):

        try:
            request_body = json.loads(request.body.decode('utf-8'))

        except JSONDecodeError: 
            return ResponseError.BadRequest(msg='Please provide json body.')

        try:
            track = createTrack(
                    user = request.current_user,
                    title = request_body.get('title'),
                    description = request_body.get('description'),
                    color = request_body.get('color'),
                    )

        except InvalidTrackTitleError:
            return ResponseError.BadRequest('Please provide title.')
        except InvalidUserError:
            return ResponseError.BadRequest('InvalidUser')
        except InvalidRatingError:
            return ResponseError.BadRequest('InvalidRating')
            
        except Exception:
            raise Exception

        try:
            serializer = TrackSerializer(result)
        except Exception:
            return ResponseError.SomethingWentWrong(err=Exception)

        return JsonResponse(
                { "track": serializer.data },
                status=201
                )


class TrackView(View):
    # /api/tracks/track_id/

    # Track details
    def get(self, request, track_id):

        user = request.current_user

        try:
            track = Track.objects.get(id=track_id, user=user)

        except Track.DoesNotExist:
            return ResponseError.NotFound(err='TrackDoesNotExist')

        try:
            serializer = TrackSerializer(track)
        except Exception:
            return ResponseError.SomethingWentWrong(err=Exception)

        return JsonResponse({ 'track': serializer.data }, safe=False)

    # Updating track
    def put(self, request, track_id):

        try:
            request_body = json.loads(request.body.decode('utf-8'))

        except JSONDecodeError: 
            return ResponseError.BadRequest(msg='Please provide json body.')

        if len(request_body.keys()) == 0:
            return ResponseError.BadRequest(msg='Please provide at least one field to update.')

        try:
            track = Track.objects.get(id=track_id)

        except Track.DoesNotExist as e:

            return ResponseError.NotFound(err='TrackDoesNotExist', msg='Track you are trying to update does not exist.')

        track.title = request_body.get('title', track.title)
        track.description = request_body.get('description', track.description)
        track.color = request_body.get('color', track.color)

        # TODO define errors
        try:
            track.save()

        except Exception:
            print(Exception)
            return ResponseError.SomethingWentWrong()

        serializer = TrackSerializer(track)

        return JsonResponse({ 
            'msg': 'Track has been updated.',
            'track': serializer.data,
            }, safe=False)


class Entry(View):

    # Get N last entries
    # /api/tracks/track_id/entry/
    def get(self, request, track_id):

        limit = int(request.GET.get('limit', 7))

        try:
            track = Track.objects.get(id=track_id, user=request.current_user)
        except Track.DoesNotExist:
            return ResponseError.NotFound(err='TrackNotFound')

        try:

            entries = TrackEntry.objects.filter(track=track_id).order_by('date').reverse()[0:limit]

            serializer = TrackEntrySerializer(entries, many=True)

        except TrackEntry.DoesNotExist:

            # TODO ?
            return ResponseError.NotFound(err='TrackEntryDoesNotExist')

        return JsonResponse({
            "limit": limit,
            'entries': serializer.data,
            })


    # Create track entry
    # /api/tracks/track_id/entry/
    def post(self, request, track_id):

        try:
            request_body = json.loads(request.body.decode('utf-8'))

        except JSONDecodeError: 
            return ResponseError.BadRequest(msg='Please provide json body.')

        try:
            track = Track.objects.get(user=request.current_user, id=track_id)

        except Track.DoesNotExist:
            return ResponseError.NotFound(err='TrackDoesNotExist')

        try:
            entry = createTrackEntry(track=track, rating=request_body.get('rating'), date=request_body.get('rating'))
        except Exception:
            ResponseError.SomethingWentWrong()
        
        serializer = TrackEntrySerializer(entry)

        return JsonResponse({"entry": serializer.data}, status=202)





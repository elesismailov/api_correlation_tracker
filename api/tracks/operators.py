
from django.utils import timezone
from django.db.utils import IntegrityError

from api.tracks.exceptions import *

from api.tracks.models import Track, TrackEntry
from users.models import CustomUser as User


def createTrack(user, title, description=None, color=None):
    """
        Creates a track.
        Returns a track or raises an error.
    """
    if not title:
        raise InvalidTrackTitleError('Please provide title')
    
    if not user:
        raise InvalidUserError('Cannot create a track with no user provided.')

    try:
        track = Track.objects.get(user=user, title=title)
        if track:
            raise TrackAlreadyExistsError('Track with that title already exists.')

    except Track.DoesNotExist as e:
        pass
    
    track = Track( user = user, title = title, description = description or '', color = color or '')

    # TODO define errors
    try:
        track.save()

    except Exception as e:
        raise e

    return track


def createTrackEntry(track, rating, date=timezone.now().date()):

    if not track:
        raise InvalidTrackError('Please provide track.')

    if not rating or not isinstance(rating, int):
        raise InvalidTrackEntryRatingError('Please provide valid rating.')

    try:
        # Search for an existing one
        entry = TrackEntry.objects.filter(
                    track=track,
                    date=date
                ).last()

        entry.rating = rating

    except TrackEntry.DoesNotExist:
        # Create new entry
        entry = TrackEntry(
                    track = track,
                    date = date,
                    rating = rating,
                )
    except AttributeError:
        entry = TrackEntry(
                    track = track,
                    date = date,
                    rating = rating,
                )
    except Exception:
        raise Exception
   
    try:
        entry.save()
    except IntegrityError:
        raise TrackEntryAlreadyExistsError('Could not save track entry.')

    except Exception as e:
        raise e

    return entry


def getTracks(user, limit=7):

    if not user:
        raise InvalidUserError('')

    tracks = Track.objects.filter(user=user).order_by('title')[0:limit]
    
    return list(tracks)


def getTrack(user, track_id):

    if not user:
        raise InvalidUserError('')

    if not track_id:
        raise InvalidTrackError('')
    
    track = Track.objects.get(user=user, id=track_id)

    return track


def getTrackEntries(track_id, limit=7):

    if not track:
        raise InvalidTrackError('Please provide valid track.')

    try:
        track = Track.objects.get(id=track_id)
    except Track.DoesNotExist:
        raise Track.DoesNotExist
    
    entries = TrackEntry.objects.filter(track=track_id).order_by('-date')[0:limit]

    return list(entries)


def updateTrack(track_id, title=None, description=None, color=None):

    if not track_id:
        raise InvalidTrackError('')

    track = Track.objects.get(id=track_id)
    
    track.title       = title or track.title
    track.description = description or track.description
    track.color       = color or track.color

    try:
        track.save()
    except Exception:
        pass

    return track




def deleteTrackEntry(entry_id):

    if not entry_id:
        raise InvalidTrackEntryError
    
    entry = TrackEntry.objects.get(id=entry_id)

    entry.delete()

    return entry










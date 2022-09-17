
from api.tracks.exceptions import *

from api.tracks.models import Track, TrackEntry
from users.models import CustomUser as User


def createTrack(user, title, description=None, color=None):
    """
        Creates a track.
        Returns an array [{"error"}, None] if an error occured.
        Returns an array [None, Data] otherwise.
    """
    if not title:
        raise NoTrackTitleError('Please provide title')
    
    if not user:
        raise NoUserError('Cannot create a track with no user provided.')

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


def createTrackEntry():
    pass 
def getTrack():
    pass
def getTrackEntries():
    pass
def getUserTracks():
    pass
def updateTrack():
    pass




def createTrack(user, title, description, color):
    """
        Creates a track.
        Returns an array [{"error"}, None] if an error occured.
        Returns an array [None, Data] otherwise.
    """
    if not title:
        return [ {"error": "NoTitle", "message": "Please provide at least title."}, None ]
    
    if not user:
        return [{"error": "NoUser", "message": "Please provide valid data."}, None]

    try:
        track = Track.objects.get(user=user, title=title)
        if track:
            return [{"error": "TrackAlreadyExists"}, None]

    except Track.DoesNotExist as e:
        pass
    
    track = Track( user = user, title = title, description = description, color = color,)

    # TODO define errors
    try:
        track.save()

    except Exception as e:
        return [{"error": "TrackAlreadyExists", "message": "Could not save into the database"}, None]

    return [None, track]


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



class InvalidTrackTitleError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidUserError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidTrackError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidTrackEntryRatingError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class TrackAlreadyExistsError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class TrackEntryAlreadyExistsError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message










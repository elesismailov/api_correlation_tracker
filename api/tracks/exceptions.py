
class NoTrackTitleError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class NoUserError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class TrackAlreadyExistsError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

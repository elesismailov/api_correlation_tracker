

from django.conf import settings

from django.http import JsonResponse

from users.models import CustomUser


class AuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        # TODO check request.header.api_key in database
        # if match return request with .current_user property

        first_user = CustomUser.objects.first()

        # assigning custom property
        request.current_user = first_user

        response = self.get_response(request)

        return response

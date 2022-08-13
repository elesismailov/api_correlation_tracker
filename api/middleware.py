

from django.conf import settings

from django.http import JsonResponse

from users.models import CustomUser


class ApiAuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        # TODO Do something about it
        if request.path[0:4] != '/api':
            response = self.get_response(request)
            return response

        api_key = request.headers.get('X-API-KEY')

        if not api_key:
            # TODO Create seperate errors class
            return JsonResponse({ 'msg': 'Please provide an api key.' }, status=400)

        user = CustomUser.objects.get(api_key=api_key)

        # Assigning custom property
        request.current_user = user

        response = self.get_response(request)

        return response

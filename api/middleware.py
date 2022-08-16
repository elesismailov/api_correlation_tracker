

from django.conf import settings
from django.http import JsonResponse

from users.models import CustomUser
from api.response_error_handler import ResponseError


class ApiAuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if request.path[0:4] != '/api':
            response = self.get_response(request)
            return response

        api_key = request.headers.get('X-API-KEY')

        if not api_key:
            return ResponseError.BadRequest(msg='Please provide an api key.')
        
        try:
            user = CustomUser.objects.get(api_key=api_key)
        except CustomUser.DoesNotExist:
            return ResponseError.NotFound(err='UserNotFound')
        except Exception:
            raise Exception

        request.current_user = user

        response = self.get_response(request)

        return response

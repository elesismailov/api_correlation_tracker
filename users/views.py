from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import json
from json.decoder import JSONDecodeError

from api.response_error_handler import ResponseError
from users.models import CustomUser


class LogIn(View):

    def post(self, request):
        
        try:
            request_body = json.loads(request.body.decode('utf-8'))

        except JSONDecodeError: 
            return ResponseError.BadRequest(msg='Please provide json body.')

        email = request_body.get('email')
        username = request_body.get('username')
        password = request_body.get('password')
        
        if not email and not username:
<<<<<<< HEAD
            return ResponseError.BadRequest(msg='Please provide valid credentials.')
=======
            return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')
>>>>>>> 79cff33 (Implement login route)

        if email:
            try:
                validate_email(email)
            except ValidationError:
<<<<<<< HEAD
                return ResponseError.BadRequest(msg='Invalid email.')
=======
                return ResponseError.BadRequest(err='InvalidEmail', msg='Invalid email.')
>>>>>>> 79cff33 (Implement login route)

            user = CustomUser.objects.get(email=email)

            if user.check_password(password):

                return JsonResponse({'key': user.api_key})

        elif username:

            user = authenticate(username=username, password=password)

            if not user:
<<<<<<< HEAD
                return ResponseError.NotFound(err='InvalidCredentials', msg='Please provide valid credentials.')

            return JsonResponse({'key': user.api_key})

        return ResponseError.NotFound(err='InvalidCredentials', msg='Please provide valid credentials.')
=======
                return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

            return JsonResponse({'key': user.api_key})

        return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

>>>>>>> 79cff33 (Implement login route)

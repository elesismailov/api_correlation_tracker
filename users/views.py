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
            return ResponseError.BadRequest(msg='Please provide valid credentials.')

        if email:
            try:
                validate_email(email)
            except ValidationError:
                return ResponseError.BadRequest(msg='Invalid email.')

            user = CustomUser.objects.get(email=email)

            if user.check_password(password):

                return JsonResponse({'key': user.api_key})

        elif username:

            user = authenticate(username=username, password=password)

            if not user:
                return ResponseError.NotFound(err='InvalidCredentials', msg='Please provide valid credentials.')

            return JsonResponse({'key': user.api_key})

        return ResponseError.NotFound(err='InvalidCredentials', msg='Please provide valid credentials.')

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.utils import IntegrityError

import json
from json.decoder import JSONDecodeError

from api.response_error_handler import ResponseError
from users.models import CustomUser


class SignUp(View):

    def post(self, request):

        try:
            request_body = json.loads(request.body.decode('utf-8'))

        except JSONDecodeError: 
            return ResponseError.BadRequest(msg='Please provide json body.')

        email = request_body.get('email')
        username = request_body.get('username')
        password = request_body.get('password')

        if not email and not username and not password:
            return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

        try:
            validate_email(email)
        except ValidationError:
            return ResponseError.BadRequest(err='InvalidEmail', msg='Invalid email.')

        user = CustomUser(email=email, username=username)

        user.set_password(password)

        try:
            user.save()
        except IntegrityError:
            return ResponseError.BadRequest(err='InvalidCredentials', msg='User with those credentials already exists.')

        except Exception:
            raise Exception

        return JsonResponse({'api_key': user.api_key})





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
            return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

        if email:
            try:
                validate_email(email)
            except ValidationError:

                return ResponseError.BadRequest(err='InvalidEmail', msg='Invalid email.')

            user = CustomUser.objects.get(email=email)

            if user.check_password(password):

                return JsonResponse({'key': user.api_key})

        elif username:

            user = authenticate(username=username, password=password)

            if not user:

                return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

            return JsonResponse({'key': user.api_key})

        return ResponseError.BadRequest(err='InvalidCredentials', msg='Please provide valid credentials.')

from django.http import JsonResponse, HttpResponse

class ResponseError:

    @staticmethod
    def NotFound(err='NotFound', msg='Not Found.'):
        
        return JsonResponse({'err': err, 'msg': msg}, status=404)

    @staticmethod
    def SomethingWentWrong(err='ServerError', msg='Something went wrong on the server.'):
        
        return JsonResponse({'msg': msg}, status=505)

    @staticmethod
    def AlreadyExists(err='AlreadyExists', msg='The resource already exists.'):
        
        return JsonResponse({'err': err, 'msg': msg}, status=400)

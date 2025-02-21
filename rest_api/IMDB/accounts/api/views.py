from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from accounts.api.serializer import RegistrationSerializer
from accounts import models
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        ser = RegistrationSerializer(data = request.data)
        data = {}
        if ser.is_valid():
            account = ser.save()
            data['response'] = 'registration succesfull!'
            data['name'] = account.username
            data['email'] = account.email
            token , created = Token.objects.get_or_create(user = account)
            data['token'] = token.key
        else:
            data = ser.errors
        return Response(data)    

class logout(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        k = {
            'Response' : 'User Deleted'
        }
        return Response(k,status=status.HTTP_200_OK)
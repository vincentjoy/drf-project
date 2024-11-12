from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializers
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializers(data=request.data)

        data = {}
        status = 201

        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Registration successful'
            token = Token.objects.create(user=account)
            data['token'] = token.key
        else:
            data = serializer.errors
            status = 400

        return Response(data, status=status)



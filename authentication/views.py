from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Authenticate(APIView):
    def post(self, request):
        return Response("Authentication Successful")
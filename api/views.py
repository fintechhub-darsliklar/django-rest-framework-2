from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

telefon = []

class MyAPi(APIView):

    def get(self, request):
        data = []
        for tel in telefon:
            data.append({
                "name": tel
            })
        return Response(data, status=status.HTTP_200_OK)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['POST'])
def github(request):
    print(request.data)
    return Response({'reply': 'gotcha'})

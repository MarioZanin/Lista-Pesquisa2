"""from django.shortcuts import render
   from django.http import JsonResponse"""

from rest_framework.views import APIView
from rest_framework.response import Response

class HomeApiView(APIView):
    def get(self, request, format=None):
        return Response({"nome": "Mario Celso", "idade": 52, "profissão": "advogado"}, status=200)

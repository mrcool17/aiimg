from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
import json
from engry import serializers
from engry.models import engryimg
from rest_framework.generics import CreateAPIView
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
# from flask.json import JSONEncoder
# Create your views here.

class uimgCreateAPIView(CreateAPIView):
    queryset = engryimg.objects.all()
    serializer_class = serializers.userSerializer

    def create(self, request, *args, **kwargs):
        #user = request.user
        serializer = serializers.userSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"Status": 400,"ResponseCode":0,"Message":"Not add"})
        self.perform_create(serializer)
        return Response({"Status": 200,"ResponseCode":1,"Message":"Data Added","Results":serializer.data})


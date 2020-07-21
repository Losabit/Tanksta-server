from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerSerializer
from .serializers import GameSerializer
from .models import Player
from .models import Game
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class PlayerList(APIView):
    def get(self, request, format=None):
        queryset = Player.objects.all().order_by('id')
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        '''
        queryset = Game.objects.all().order_by('id')
        new_serializer = GameSerializer(queryset, many=True)
        for data in new_serializer.data:
            if data['players'] < 4 and data['turn_id'] == None:
                request.data["play_on"] = data['id']
                print(request.data)
                break
        '''       
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PlayerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PlayerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if "want_to_play" in request.data:
                print(request.data["want_to_play"])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
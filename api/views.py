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
        party_start = False
        if not "play_on" in request.data:
            queryset = Game.objects.all().order_by('id')
            new_serializer = GameSerializer(queryset, many=True)
            for data in new_serializer.data:
                if data['players'] < 4 and data['turn_id'] == None:
                    request.data["play_on"] = data['id']
                    link = Game.objects.get(pk=data['id'])
                    data["players"] += 1
                    request.data["order"] = data["players"]
                    if data["players"] == 4:
                        party_start = True
                    else:
                        new_serializer = GameSerializer(link, data=data)    
                        if new_serializer.is_valid():
                            new_serializer.save()
                    break
            if not "play_on" in request.data:
                dic = {"name": "newGame", "players": 1, "players_want_play" : 0}    
                new_serializer = GameSerializer(data=dic)    
                if new_serializer.is_valid():
                    result = new_serializer.save()
                    request.data["play_on"] = result.id
                    request.data["order"] = 1

        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            if party_start:
                data["turn_id"] = result.id
                self.initGame(data["id"])
                new_serializer = GameSerializer(link, data=data)    
                if new_serializer.is_valid():
                    new_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def initGame(self, game_id):
        queryset = Player.objects.all().order_by('id')
        new_serializer = PlayerSerializer(queryset, many=True)
        i = 0
        for data in new_serializer.data:
            if data['play_on'] == game_id:
                data["health"] = 100
                data["canon_orientation"] = 90.0
                data["shoot"] = False
                data["pos_x"] = float(i * 300 + 150)
                data["pos_y"] = 650.0 
                link = Player.objects.get(pk=data['id'])
                serializer = PlayerSerializer(link, data=data)    
                if serializer.is_valid():
                    serializer.save()
                i += 1

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
            result = serializer.save()
            if "end_of_turn" in request.data:
                if request.data['end_of_turn'] == True:
                    link = Game.objects.get(pk=serializer.data["play_on"])
                    game_serializer = GameSerializer(link)    
                    data_game = game_serializer.data
                    if data_game["turn_id"] == pk:
                        queryset = Player.objects.all().order_by('id')
                        player_serializer = PlayerSerializer(queryset, many=True)
                        for data in player_serializer.data:
                            if data['id'] == data_game["turn_id"]:
                                order = data['order'] + 1
                                break
                        if order > data_game['players']:
                            order = 1
                        
                        for data in player_serializer.data:
                            if 'order' in data:
                                if data['order'] == order and data['play_on'] == data_game['id']:
                                    data_game['turn_id'] = data['id']
                                    request.data["shoot"] = False
                                    new_serializer = GameSerializer(link, data=data_game)
                                    if new_serializer.is_valid():
                                        new_serializer.save()
                                    else:
                                        print("error")
                                    break
                    else:
                        print("it's not your turn")

            if "want_to_play" in request.data:
                if request.data["want_to_play"] == True:
                    link = Game.objects.get(pk=serializer.data["play_on"])
                    new_serializer = GameSerializer(link)    
                    data = new_serializer.data
                    if "turn_id" in data:
                        data["players_want_play"] += 1
                        if data["players_want_play"] == data["players"]:
                            data["turn_id"] = result.id
                            self.initGame(data["id"])
                        new_serializer = GameSerializer(link, data=data)
                        if new_serializer.is_valid():
                            new_serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PlayerSerializer(snippet)
        link = Game.objects.get(pk=serializer.data["play_on"])
        new_serializer = GameSerializer(link)    
        data = new_serializer.data
        data["players"] -= 1
        serializer = GameSerializer(link, data=data)
        if serializer.is_valid():
            serializer.save()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def initGame(self, game_id):
        queryset = Player.objects.all().order_by('id')
        new_serializer = PlayerSerializer(queryset, many=True)
        i = 0
        for data in new_serializer.data:
            if data['play_on'] == game_id:
                data["health"] = 100
                data["canon_orientation"] = 90.0
                data["shoot"] = False
                data["pos_x"] = float(i * 300 + 150)
                data["pos_y"] = 650.0 
                link = Player.objects.get(pk=data['id'])
                serializer = PlayerSerializer(link, data=data)    
                if serializer.is_valid():
                    serializer.save()
                i += 1

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
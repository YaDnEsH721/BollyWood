from django.shortcuts import render, redirect
import random, string

def index(request):
    return render(request, 'index.html')

def create_game(request):
    player_name = request.POST.get('player')
    return render(request, 'create_game.html', {'player_name':player_name})

def create_room(request):
    players = request.POST.get('player')
    guess_duration = request.POST.get('guess_duration')
    no_of_round = request.POST.get('no_of_round')
    host_player = request.POST.get('player_name')
    room_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    #store room details in session
    request.session['players'] = players
    request.session['guess_duration'] = guess_duration
    request.session['no_of_round'] = no_of_round
    request.session['host_player'] = host_player
    request.session['room_code'] = room_code
    return render(request, 'main_game.html', {'players':players, 'guess_duration':guess_duration, 'no_of_round':no_of_round, 'host_player':host_player, 'room_code':room_code})

def join_game(request):
    player_name = request.POST.get('player1')
    return render(request, 'join_game.html', {'player_name':player_name})
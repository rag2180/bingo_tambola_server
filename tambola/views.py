from django.shortcuts import render
from django.http import HttpResponse

"""
Reference Link: https://www.bytetales.co/housie-tambola-ticket-generator-using-python/
"""


def home_page(request):
    return HttpResponse("Home Page")


def create_game(request):
    return HttpResponse("Create Game")


def generate_ticket_for_user(request, game_id, user_id):
    return HttpResponse("Generating Ticket for Game: {} User:{}".format(game_id, user_id))


def print_ticket(request, ticket_id):
    return HttpResponse("Printing Ticket: {}".format(ticket_id))


def generate_number_for_game(request, game_id):
    return HttpResponse("Generating Random Number for game: {}".format(game_id))


def all_drawn_numbers_for_game(request, game_id):
    return HttpResponse("All Drawn Numbers for game: {}".format(game_id))


def game_stats(request, game_id):
    return HttpResponse("Game Stats - {}".format(game_id))
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Player, Ticket, Game, TicketNumbers, GameNumbers

admin.site.register(Player)
admin.site.register(Ticket)
admin.site.register(Game)
admin.site.register(TicketNumbers)
admin.site.register(GameNumbers)

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Game(models.Model):
    game_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return self.game_id


class Player(models.Model):
    name = models.CharField(max_length=255, unique=False)
    game_id = models.ForeignKey(to=Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    player_id = models.ForeignKey(to=Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class TicketNumbers(models.Model):
    ticket_id = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MaxValueValidator(90), MinValueValidator(1)])

    def __str__(self):
        return str(self.ticket_id)+"_"+str(self.number)


class GameNumbers(models.Model):
    game_id = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MaxValueValidator(90), MinValueValidator(1)])

    def __str__(self):
        return str(self.game_id.id)+"_"+str(self.number)
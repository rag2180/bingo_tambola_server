from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.home_page, name='home'),
    path('api/game/create', views.create_game, name='create_game'),
    path('api/game/<int:game_id>/ticket/<int:user_id>/generate', views.generate_ticket_for_user, name='generate_ticket'),
    path('ticket/<int:ticket_id>', views.print_ticket, name='print_ticket'),
    path('api/game/<int:game_id>/number/random', views.generate_number_for_game, name='generate_number'),
    path('api/game/<int:game_id>/numbers', views.all_drawn_numbers_for_game, name='all_drawn_numbers'),
    path('api/game/<int:game_id>/stats', views.game_stats, name='game_stats'),
]
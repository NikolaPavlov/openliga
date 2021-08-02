from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_games', views.all_games, name='all_games'),
    path('next_day_games', views.next_day_games, name='next_day_games'),
    path('win_loss_ratio', views.win_loss_ratio, name='win_loss_ratio'),
]

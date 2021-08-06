from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('win_loss_ratio', views.win_loss_ratio, name='win_loss_ratio'),
    path('team_search', views.team_search, name='team_search'),
]

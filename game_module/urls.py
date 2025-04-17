from django.urls import path
from game_module import views

urlpatterns = [
    path('game1',views.memory_game,name = 'see_game'),
    path('game2',views.memory_game2,name = '2048_game'),
]
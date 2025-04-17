from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz-riazi', views.quizRiaziPage, name='quiz-riazi-page'),
    path('quiz-farsi', views.quizFarsiPage, name='quiz-farsi-page'),
    path('add_quiz', views.addQuiz, name='add_quiz'),
    path('startFarsiQuiztion', views.startFarsiQuiztion, name='startFarsiQuiztion'),
    path('startRiaziQuiztion', views.startRiaziQuiztion, name='startRiaziQuiztion'),

    # path('start_quiz', views.start_quiz, name='start_quiz'),
    path('quiz_information', views.quizInformation, name='quiz_information'),
]

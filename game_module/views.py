import math

from django.shortcuts import render, redirect
# import tkinter as tk
# import random
from quiz_module.models import Quiz
from .colors import Game

def memory_game(request):
    farsi_scors = []
    farsi = Quiz.objects.filter(quizdetail__lesson_id=2).all()
    for exam in farsi:
        # print('farsfffi_score : ', exam.quizdetail_set.all()[0].score)
        farsi_scors.append(exam.quizdetail_set.all()[0].score)
    if len(farsi_scors) == 0:
        ave_farsi_scors = sum(farsi_scors) / 1
    else:
        ave_farsi_scors = sum(farsi_scors) / len(farsi_scors)

    need_farsi_scor = 3 - math.ceil(ave_farsi_scors)
    context = {'need_score':need_farsi_scor}
    return render(request,'game_module/memory_game_page.html',context)


def memory_game2(request):
    riazi_scors = []
    farsi = Quiz.objects.filter(quizdetail__lesson_id=1).all()
    for exam in farsi:
        # print('farsi_score : ', exam.quizdetail_set.all()[0].score)
        riazi_scors.append(exam.quizdetail_set.all()[0].score)
    print('riazi_score : ', riazi_scors)
    if len(riazi_scors ) == 0:
        ave_riazi_scor = sum(riazi_scors ) / 1
    else:
        ave_riazi_scor = sum(riazi_scors ) / len(riazi_scors )

    need_riazi_scor = 3 - math.ceil(ave_riazi_scor)
    print('need_score : ', need_riazi_scor)

    context = {'need_score': need_riazi_scor}
    return render(request,'game_module/2048-page.html',context)

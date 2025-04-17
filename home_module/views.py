from django.db.models import Avg
from django.shortcuts import render
from django.views import View
from account_module.models import User
from quiz_module.models import Quiz, QuizDetail
from utils.calculate_average import calc_avg


def home_page(request):
    current_user = User.objects.filter(id=request.user.id).first()
    if request.user.is_authenticated:
        quiz_farsi = Quiz.objects.filter(student_id= current_user.id , quizdetail__lesson__title = "فارسی").all()
        quiz_riazi = Quiz.objects.filter(student_id= current_user.id , quizdetail__lesson__title= "ریاضی").all()
        # score_quiz_farsi = QuizDetail.objects.filter(lesson__title='فارسی' ).all()
        # score_quiz_riazi = QuizDetail.objects.filter(lesson__title='ریاضی' ).all()
        riazi_average_mark, farsi_average_mark, riazi_scores , farsi_scores = calc_avg(quiz_farsi, quiz_riazi)

        context = {'current_user': current_user,
                   'len_f':quiz_farsi.count(),
                   'len_r':len(quiz_riazi),
                   'farsi_average': farsi_average_mark,
                   'riazi_average': riazi_average_mark,
                   }
        return render(request, 'home_module/home_page.html', context)
    if not request.user.is_authenticated:
        return render(request, 'home_module/home_page.html')

        # if quiz_farsi.count() != 0:
        #     avg_f = score_quiz_farsi.aggregate(Avg('score'))
        #     avg_f = float("%6.2f" % avg_f['score__avg'])
        # else:
        #     avg_f = 0
        #
        # if quiz_riazi.count() != 0:
        #     avg_r = score_quiz_riazi.aggregate(Avg('score'))
        #     avg_r = float("%6.2f" % avg_r['score__avg'])
        # else:
        #     avg_r = 0

def header_component(request):
    user = request.user
    current_user = User.objects.filter(id=request.user.id).first()
    print('current_user is : ', current_user, 'user is: ', user)
    context = {'current_user': current_user, 'user': user}
    return render(request, 'shared/header_component.html', context)




   # for quiz in quiz_farsi:
        #     for q in quiz.quizdetail_set.all():
        #         # print('score in quiz_farsi is: ', q.score)
        #         farsi_scores.append(q.score)
        # if len(farsi_scores) != 0:
        #     farsi_average = sum(farsi_scores) / len(farsi_scores)
        #     farsi_average_mark = float("%6.2f" % farsi_average)
        # else:
        #     farsi_average_mark = sum(farsi_scores) / 1

# class headerComponent(View):
#     def get(self, request):
#         current_user = User.objects.filter(request.user.id).first()
#         context = {'current_user':current_user}
#         return render(request, 'shared/header_component.html',context)
#
import json
import random
from datetime import time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account_module.models import User
from utils.makeQuiz import make_quiz
# from quiz_module import before_exams.txt
from .forms import make_quiz_form
from .models import QuestionsBank, Lesson, Quiz, QuizDetail
from jalali_date import datetime2jalali, date2jalali
from django.forms.models import model_to_dict
lesson_is_running = {}

def quizPage(request):
    form = make_quiz_form(request.POST)
    context = {'q_form': form}
    return render(request, 'quiz_module/quiz-riazi-page.html', context)


# def quizRiaziPage(request):
#     current_user = User.objects.filter(id=request.user.id).first()
#     current_quiz = Quiz.objects.filter(student_id=current_user.id, is_finished=False).first()
#     file_riazi_path = 'utils/all_before_exams/before_riazi_exams' + f'{current_user.id}' + '.txt'
#     if current_quiz is None:
#         print('آزمون قبلی تمام شده است ..')
#         new_quiz = Quiz.objects.create(student_id=current_user.id, is_finished=False)
#         qbank = QuestionsBank.objects.filter(lesson__title='ریاضی')

#         # I creat a function for make a quiz
#         context = make_quiz('riazi',qbank,new_quiz,current_user,file_riazi_path)

#         new_quiz.doing_exam = context
#         new_quiz.save()
#         return render(request, 'quiz_module/quiz-riazi-page.html', context)
#     else:
#         if len(current_quiz.doing_exam) == 0:
#             return render(request, 'quiz_module/quiz-riazi-page.html',{'is_context_empty':'f'})
#         d = eval(current_quiz.doing_exam)
#         if d != 0 and d.get('lesson') == 'riazi':
#             return render(request, 'quiz_module/quiz-riazi-page.html', d)
#         return render(request, 'quiz_module/quiz-farsi-page.html')


def quizRiaziPage(request):
    current_user = User.objects.filter(id=request.user.id).first()
    # context = {"current_user":current_user,'is_context_empty': 't'}
    return render(request, 'quiz_module/preperty-quiz-riazi-page.html')

def quizFarsiPage(request):
    current_user = User.objects.filter(id=request.user.id).first()
    context = {"current_user":current_user,'is_context_empty': 't'}
    return render(request, 'quiz_module/quiz-farsi-page.html',context)


def startFarsiQuiztion(request):
    print('start farsi ..................')
    farsi_start_time = request.GET.get('farsi_start_time')
    current_time = request.GET.get('current_time')
    current_user = User.objects.filter(id=request.user.id).first()
    print('user id: ',current_user.id)
    current_quiz = Quiz.objects.filter(student_id=current_user.id, is_finished=False).first()
    file_farsi_path = 'utils/all_before_exams/before_farsi_exams' + f'{current_user.id}' + '.txt'
    if current_quiz is None:
        print('آزمون قبلی تمام شده است ..')
        new_quiz = Quiz.objects.create(student_id=current_user.id, is_finished=False)
        qbank = QuestionsBank.objects.filter(lesson__title='فارسی')

        # I creat a function for make a quiz
        context = make_quiz('farsi',farsi_start_time, qbank, new_quiz, current_user, file_farsi_path)

        new_quiz.doing_exam = context
        new_quiz.save()
        return render(request, 'quiz_module/quiz-farsi-page.html', context)
    else:
        if len(current_quiz.doing_exam) == 0:
            print('else if 1 .....')
            return render(request, 'quiz_module/quiz-farsi-page.html', {'is_context_empty': 'f'})
        d = eval(current_quiz.doing_exam)
        if d != 0 and d.get('lesson') == 'farsi':
            print('else if 2 .....')
            return render(request, 'quiz_module/quiz-farsi-page.html', d)
        return render(request, 'quiz_module/quiz-farsi-page.html')

def startRiaziQuiztion(request):
    riazi_start_time = request.GET.get('riazi_start_time')
    current_time = request.GET.get('current_time')
    current_user = User.objects.filter(id=request.user.id).first()
    current_quiz = Quiz.objects.filter(student_id=current_user.id, is_finished=False).first()
    file_riazi_path = 'utils/all_before_exams/before_riazi_exams' + f'{current_user.id}' + '.txt'
    if current_quiz is None:
        print('آزمون قبلی تمام شده است ..')
        new_quiz = Quiz.objects.create(student_id=current_user.id, is_finished=False)
        qbank = QuestionsBank.objects.filter(lesson__title='ریاضی')

        # I creat a function for make a quiz
        new_context = make_quiz('riazi',riazi_start_time, qbank, new_quiz, current_user, file_riazi_path)
        # print('context: ', context,type(context))
        new_quiz.doing_exam = new_context
        new_quiz.save()
        return render(request, 'quiz_module/quiz-riazi-page.html', new_context)
    else:
        if len(current_quiz.doing_exam) == 0:
            return render(request, 'quiz_module/quiz-riazi-page.html', {'is_context_empty': 'f'})
        d = eval(current_quiz.doing_exam)
        if d != 0 and d.get('lesson') == 'riazi':
            return render(request, 'quiz_module/quiz-riazi-page.html', d)
        return render(request, 'quiz_module/quiz-riazi-page.html')

# def quizFarsiPage(request):
#     current_user = User.objects.filter(id=request.user.id).first()
#     current_quiz = Quiz.objects.filter(student_id=current_user.id, is_finished=False).first()
#     file_farsi_path = 'utils/all_before_exams/before_farsi_exams' + f'{current_user.id}' + '.txt'
#     if current_quiz is None:
#         new_quiz = Quiz.objects.create(student_id=current_user.id, is_finished=False)
#         qbank = QuestionsBank.objects.filter(lesson__title='فارسی')
#         # I creat a function for make a quiz
#         context = make_quiz('farsi', qbank, new_quiz, current_user, file_farsi_path)
#         new_quiz.doing_exam = context
#         new_quiz.save()
#         return render(request, 'quiz_module/quiz-farsi-page.html', context)
#     else:
#         if len(current_quiz.doing_exam) == 0:
#             return render(request, 'quiz_module/quiz-farsi-page.html', {'is_context_empty': 'f'})
#         d = eval(current_quiz.doing_exam)
#         if d != 0 and d.get('lesson') == 'farsi':
#             return render(request, 'quiz_module/quiz-farsi-page.html', d)
#         return render(request, 'quiz_module/quiz-farsi-page.html')


def addQuiz(request):
    current_user = User.objects.filter(id=request.user.id).first()
    print('current_user in add quiz: ', current_user.email)
    leson = request.GET.get('lesson')
    scor = request.GET.get('score')
    time1 = request.GET.get('time1')
    time2 = request.GET.get('time2')
    time3 = request.GET.get('time3')
    month = request.GET.get('month')
    day = request.GET.get('day')
    farsi_date = request.GET.get('farsi_date')
    print('leson is: ', leson, 'score is: ', scor,'time1: ',time1,"time2: ", time2,"time3: ", time3)
    lesson_id = Lesson.objects.filter(title__exact=leson).first().id
    current_quiz, created = Quiz.objects.get_or_create(student_id=current_user.id, is_finished=False)
    current_quiz_detail = current_quiz.quizdetail_set.filter(lesson_id=lesson_id).first()
    if current_quiz_detail is not None:
        current_quiz_detail.numbers_doing_exam += 1
        current_quiz_detail.save()
        print('وجود دارد جزییات ازمون')
    else:
        print(' before create وجود ندارد جزییات ازمون')
        new_quiz_detail = QuizDetail(lesson_id=lesson_id, quiz_id=current_quiz.id, score=scor, numbers_doing_exam=1)
        new_quiz_detail.save()

    current_quiz.is_finished = True
    current_quiz.doing_exam =''
    current_quiz.save()
    context = {'quiz': leson, 'score': scor}
    return redirect('/')
    # return render(request, 'quiz_module/user_quiz_information.html', context)


def quizInformation(request):
    current_user = User.objects.filter(id=request.user.id).first()
    print('current_user: ', current_user.id)
    quiz_farsi = Quiz.objects.filter(student_id=current_user.id, quizdetail__lesson=2)
    quiz_riazi = Quiz.objects.filter(student_id=current_user.id, quizdetail__lesson=1)
    print('quiz farsi is: ', quiz_farsi, len(quiz_farsi))
    print('quiz riazi is: ', quiz_riazi)
    context = {'quiz_farsi': quiz_farsi, 'quiz_riazi': quiz_riazi, 'current_user': current_user}
    return render(request, 'quiz_module/user_quiz_information.html', context)








# year = request.GET.get('year')
# month = request.GET.get('month')
# day = request.GET.get('day')
# date = f'{year}-{month}-{day} 00:00'
# date2 = time.time()
# date2 = datetime2jalali(date).strftime('%y/%m/%d _ %H:%M:%S')
# print('date is: ', date, 'type data is: ', date2)
# print('date is: ', date)
# print('year is: ', year)
# print('month is: ', month)
# print('day is: ', day)


# def quizRiaziPage(request):
#     user = request.user
#     i = 0
#     flist = [1,2,3,4,5]
#     list_of_question = []
#     list_of_option = []
#     list_of_answer = []
#     form = make_quiz_form(request.POST)
#     qbank = QuestionsBank.objects.filter(lesson__title='ریاضی')
#     while i < 100:
#         number_of_question = random.randint(0, len(qbank) - 1)
#         random_question = qbank[number_of_question]
#         option1 = random_question.option1
#         option2 = random_question.option2
#         option3 = random_question.option3
#         option4 = random_question.option4
#         answer = random_question.answer
#         options = [option1, option2, option3, option4]
#         if options not in list_of_option:
#             list_of_option.append(options)
#             list_of_answer.append(answer)
#         print('option1,option2,option3,option4 are: ', option1,option2,option3,option4)
#         print('list_of_option: ', list_of_option)
#         print('list_of_answer: ', list_of_answer)
#         if random_question not in list_of_question:
#             list_of_question.append(random_question)
#             if len(list_of_question) == 6:
#                 break
#         i += 1
#     print('list_of_question : ', list_of_question)
#     context = {'user': user,
#                'q_form': form,
#                'f_list':flist,
#                'questions': list_of_question,
#                'options': list_of_option,
#                'answers': list_of_answer
#                }
#     return render(request, 'quiz_module/quiz-riazi-page.html', context)


# context = model_to_dict(context, fields=[field.name for field in context._meta.fields])
# with open('save_last_exam.json', 'w') as f1:
#     json.dump(context,f1)
# with open('save_last_exam.json', 'r') as f2:
#     data = json.load(f2)
# d = data
# print('data: ', d)

# json_acceptable_string = current_quiz.doing_exam.replace("'", "\"")
# d = json.loads(json_acceptable_string)
# print('json_acceptable_string is: ', json_acceptable_string,"type: ",type(json_acceptable_string))
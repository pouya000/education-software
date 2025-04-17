from django.db import models
from jalali_date import date2jalali
from account_module.models import User
import json

class Lesson(models.Model):
    title = models.CharField(max_length=300, verbose_name='درس', null=True, blank=True)

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس ها'

    def __str__(self):
        return self.title


class AducationaLevel(models.Model):
    title = models.CharField(max_length=30, verbose_name='مقطع تحصیلی')

    class Meta:
        verbose_name = 'مقطع تحصیلی'
        verbose_name_plural = 'مقاطع تحصیلی'

    def __str__(self):
        return self.title


class QuestionsBank(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    aducational_level = models.ForeignKey('AducationaLevel', on_delete=models.CASCADE)
    difficulty = models.TextField(max_length=300, verbose_name='درجه سختی')
    question = models.TextField(max_length=300, verbose_name='سوال')
    option1 = models.TextField(max_length=300, null=True, blank=True, verbose_name='گزینه 1')
    option2 = models.TextField(max_length=300, null=True, blank=True, verbose_name='گزینه 2')
    option3 = models.TextField(max_length=300, null=True, blank=True, verbose_name='گزینه 3')
    option4 = models.TextField(max_length=300, null=True, blank=True, verbose_name='گزینه 4')
    answer = models.TextField(max_length=300, null=True, blank=True, verbose_name=' جواب')

    class Meta:
        verbose_name = ' سوالات'
        verbose_name_plural = 'بانک سوالات'

    def __str__(self):
        return self.question


class Quiz(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='دانش آموز')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    doing_exam = models.TextField(blank=True, null=True, default='{}')
    is_finished = models.BooleanField(null=True, blank=True, verbose_name=' تمام شده/نشده')

    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون ها'

    def get_jalali_date(self):
        return date2jalali(self.date)

    def get_jalali_time(self):
        return self.date.strftime('%H:%M:%S ')

    def get_jalali_create_date(self):
        return date2jalali(self.date)

    def __str__(self):
        return self.student.first_name


# class QuizQuestions(models.Model):
#     quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE, verbose_name=' سوالات امتحان  ')
#     ques1 = models.CharField(max_length=100,verbose_name='سوال اول')
#
#     ques2 = models.CharField(max_length=100,verbose_name='سوال دوم')
#     ques3 = models.CharField(max_length=100,verbose_name='سوال سوم')
#     parent = models.ForeignKey(to='ArticleComment', on_delete=models.CASCADE, null=True, blank=True,
#                                verbose_name='والد')
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
#     # text = models.CharField(max_length=300, verbose_name='متن نظر', null=True, blank=True)
#     # create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')


class QuizDetail(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, verbose_name='درس')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, default=0, verbose_name='امتیاز درس')
    numbers_doing_exam = models.IntegerField(null=True, blank=True, default=0, verbose_name='دفعات شرکت در آزمون')

    # questions = models.ForeignKey(to ='QuestionsBank',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'جزییات آزمون'
        verbose_name_plural = 'جزییات آزمون ها'

    def __str__(self):
        return self.lesson.title


#
# models.py
#
# import json

# class Item(models.Model):
#     data = models.TextField(blank=True, null=True, default='{}')
#
#     def save(self, *args, **kwargs):
#         ## load the current string and
#         ## convert string to python dictionary
#         data_dict = json.loads(self.data)
#
#         ## do something with the dictionary
#         for something in somethings:
#             data_dict[something] = some_function(something)
#
#         ## if it is empty, save it back to a '{}' string,
#         ## if it is not empty, convert the dictionary back to a json string
#         if not data_dict:
#             self.data = '{}'
#         else:
#             self.data = json.dumps(data_dict)
#
#
#         super(Item, self).save(*args, **kwargs)

# روش لود کردن شیء جیسون درون پایتون چنین است
# import json
# obj = json.loads("""{
# "firstName": "Alice",
# "lastName": "Hall",
# "age": 35
# }""")
#
# firstName = obj["firstName"]
# lastName = obj["Hall"]
# age = obj["age"]
from django.contrib import admin
from quiz_module import models

class QuestionsBankAdmin(admin.ModelAdmin):
    list_display = ['__str__','lesson','aducational_level','difficulty','answer']
    class Meta:
        model = models.QuestionsBank

class QuizAdmin(admin.ModelAdmin):
    list_display = ['student','date','is_finished']
    class Meta:
        model = models.Quiz

class QuizDetailAdmin(admin.ModelAdmin):
    list_display = ['quiz','lesson','score','numbers_doing_exam']
    class Meta:
        model = models.QuizDetail


admin.site.register(models.QuestionsBank,QuestionsBankAdmin)
admin.site.register(models.Lesson)
admin.site.register(models.AducationaLevel)
admin.site.register(models.Quiz,QuizAdmin)
admin.site.register(models.QuizDetail,QuizDetailAdmin)



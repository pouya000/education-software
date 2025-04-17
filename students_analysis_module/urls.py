from django.urls import path
from . import views

urlpatterns = [
    path('student_analysis',views.student_analysis,name="student_analysis" ),
    # path('student_analysis_all_lessons',views.student_analysis_all_lessons,name="student_analysis_all_lessons" ),
]

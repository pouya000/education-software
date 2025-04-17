from django.urls import path
from . import views

urlpatterns = [
    path('edit_profile', views.editProfile.as_view(),name='edit_profile'),
]
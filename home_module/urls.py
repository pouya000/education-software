from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page" ),
    path('header', views.header_component, name='header_component'),
    # path('header', views.headerComponent.as_view(), name='header_component'),
]

from django.contrib import admin
from django.urls import path,include
from myapp import views
# from .views import hi

urlpatterns = [
    path('',views.news_view, name = 'news_view')
]

from django.urls import path
from .views import nippoListView, success_page

urlpatterns = [
    path("", nippoListView),
    path('success/', success_page, name='success_page'),



]

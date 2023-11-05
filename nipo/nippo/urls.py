from django.urls import path
from .views import sendbygmailView, success_page, copytempView

urlpatterns = [
    path("sendbygmail", sendbygmailView),
    path("copytemp",copytempView),
    path('success/', success_page, name='success_page'),



]

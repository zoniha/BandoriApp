from django.urls import path
from . import views


app_name = 'afterglow'

urlpatterns = [
    path('', views.TopPageView.as_view(), name='toppage'),
]

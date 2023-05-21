from django.urls import path

from . import views

app_name = 'consumer'

urlpatterns = [
    path('create/', views.CreateConsumerView.as_view(), name='create'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles ,name='profiles'),
    path('',views.details ,name='details'),
    ]
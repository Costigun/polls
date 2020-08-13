from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers
from questionnaire import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
router = routers.DefaultRouter()
router.register('questions',QuestionListView)

urlpatterns = [
    path('questions/<int:pk>/answers/', QuestAnswerView.as_view(), name='answer_questions'),
    path('polls/',views.polls_list),
    path('polls/<int:pk>/',views.polls_post),
    path('complete_polls/<int:pk>/',CompletedPollsView.as_view())
]

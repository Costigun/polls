import random
import string

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .services import *
from .models import *
from .serializers import *
from rest_framework import viewsets, status


# Create your views here.


@api_view(['GET'])
def polls_list(request, *args, **kwargs):
    if request.method == 'GET':
        global user_id
        user_id = random.randint(0, 100)
        print(user_id)
        poll = Poll.objects.all()
        serializer = PollSerializer(poll,many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


@api_view(['POST'])
def polls_post(request,*args,**kwargs):
    if request.method == 'POST':

        print(request.user.id)

        serializer = AnswerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            answer_field = request.data.pop('answer_field')
            question_id = request.data.pop('question_id')
            QuetionService.answer_quest(user_id, question_id, answer_field)
            return Response({'data':'Successfully created! Your ID is %s' % user_id }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class QuestAnswerView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        answers = QuetionService.get_answers(kwargs['pk'])
        data = AnswerSerializer(answers, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = AnswerCreateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = random.randint(0,100)
            answer_field = serializer.data.get('answer_field')
            idea_id = kwargs['pk']
            QuetionService.answer_quest(user_id,idea_id, answer_field)
            return Response('Successfully created! Your ID is %s' % user_id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class QuestionListView(ReadOnlyModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CompletedPollsView(APIView):

    def get(self,request,**kwargs):

        polls = QuestAnswerModel.objects.filter(user_id=kwargs['pk'])
        serializer = QuestAnsSerializer(polls, many=True)
        return Response(serializer.data)


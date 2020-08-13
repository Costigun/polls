from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id','text')


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)
    poll_id = serializers.PrimaryKeyRelatedField(read_only=True)
    poll_description = serializers.CharField(source='poll.description')

    class Meta:
        model = Question
        fields = ('id','poll_id','poll_description','description','question_type','answer')


class PollSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id','description','start_date','end_date','question')


class QuestAnsSerializer(serializers.ModelSerializer):
    poll = serializers.CharField(source='question_io.poll.description')
    question_io = serializers.CharField(source='question_io.description')

    class Meta:
        model = QuestAnswerModel
        fields = ('id','poll','user_id','question_io','answer_io')


class AnswerCreateSerializer(serializers.Serializer):
    answer_field = serializers.CharField(allow_blank=False)

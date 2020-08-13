from django.db.models import QuerySet
from rest_framework.exceptions import NotFound

from .models import *


class AnswerService:
    @classmethod
    def filter(cls, **filters):
        return Answer.objects.filter(**filters)

    @classmethod
    def create_answer(cls, user_id:int,question: Question, answer: str):
        QuestAnswerModel.objects.create(user_id=user_id,question_io=question,answer_io=answer)


class QuetionService:
    @classmethod
    def filter(cls, **filters) -> QuerySet:
        return Question.objects.filter(**filters)

    @classmethod
    def get_answers(cls, question_id: int) -> QuerySet:
        questions = cls.filter(id=question_id).first()
        if not questions:
            raise NotFound
        return AnswerService.filter(question=question_id)

    @classmethod
    def answer_quest(cls,user_id:int,question_id: int, answer: int,):
        service = QuetionService.filter(id=question_id).first()
        if not service:
            raise NotFound
        AnswerService.create_answer(user_id,service,answer)

from django.db import models

# Create your models here.

quest_type = [
    ('One', 'Один ответ'),
    ('One_Text', 'Текстовый ответ'),
    ('Mult', 'Несколько вариантов ответа'),
]


class Poll(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.TextField()


class Question(models.Model):
    description = models.TextField()
    question_type = models.CharField(max_length=50,choices=quest_type)
    poll = models.ForeignKey(Poll,on_delete=models.PROTECT,related_name='question')

    def __str__(self):
        return self.description


class Answer(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey(Question,on_delete=models.PROTECT,related_name='answer')

    def __str__(self):
        return self.text


class QuestAnswerModel(models.Model):
    user_id = models.IntegerField(unique=True)
    question_io = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question')
    answer_io = models.CharField(max_length=50)


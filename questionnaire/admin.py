from django.contrib import admin
from .models import *
from nested_inline.admin import NestedStackedInline,NestedModelAdmin
# Register your models here.


admin.site.register([Question,Answer])


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 1
    fk_name = 'question'


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1
    fk_name = 'poll'
    inlines = [AnswerInline]


class PollAdmin(NestedModelAdmin):
    model = Poll
    inlines = [QuestionInline,]
    list_display = ['description','end_date']


admin.site.register(Poll,PollAdmin)


class QuestionDisplay(admin.ModelAdmin):
    model = QuestAnswerModel
    list_display = ['user_id','question_io','answer_io']

admin.site.register(QuestAnswerModel,QuestionDisplay)

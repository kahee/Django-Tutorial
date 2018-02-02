from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    # 가장 최근 발행된 최대 4개의  Question 목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 쉼표 단위로 구분된 Question 목록의 각 항목의 question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in lastest_question_list])

    context = {
        'latest_question_list': latest_question_list,
    }
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
    'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "Your,re looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

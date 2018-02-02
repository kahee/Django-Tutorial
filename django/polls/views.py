from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def results(request, question_id):
    response = "Your,re looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, qestion_id):
    return HttpResponse("You're voting on question %s." %qestion_id)
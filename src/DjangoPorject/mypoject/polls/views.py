from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    latest_question_list =  Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    #     # print(question)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})


def results(request, quesion_id):
    respose = "You're looking at the results of quesiont %s."
    return HttpResponse(respose%quesion_id)


def vote(request, quetion_id):
    return HttpResponse("You're looking at the results of quesiont %s."%quetion_id)
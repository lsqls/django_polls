# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from .models import question,choice

# Create your views here.
def index(request):
    question_lists=question.objects.all()
    content={"question_lists":question_lists}
    return render(request,"polls/index.html",content)
def detail(request,question_id):
    Question=get_object_or_404(question,pk=question_id)
    choice_lists=Question.choice_set.all()
    content={"question":Question,'choice_lists':choice_lists}
    return render(request,"polls/detail.html",content)
def vote(request,question_id):
    p=get_object_or_404(question,pk=question_id)
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
    selected_choice.vote += 1
    selected_choice.save()
    return HttpResponse("vote success")


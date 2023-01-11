from django.shortcuts import render
from django.http import JsonResponse
from .RuleStructure.Questions import lit_question
from django.core import serializers
import json

# assuming obj is a model instance


def hello(request):
    return JsonResponse({'foo': 'bar'})


def questions(request):
    # ques = json.dumps(questions, indent=2)
   
    return JsonResponse({"questions": lit_question})

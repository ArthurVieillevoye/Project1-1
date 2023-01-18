from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .RuleStructure.Questions import lit_question
from .RuleStructure.Examples import toy_examples
from django.core import serializers
import json

# assuming obj is a model instance


from http import HTTPStatus

class HttpResponseNoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT

def hello(request):
    return JsonResponse({'foo': 'bar'})


def questions(request):
    return JsonResponse({"questions": lit_question})

def examples(request):
    return JsonResponse({"examples": toy_examples})

def examplesTwo(request):
    return JsonResponse({"examples": toy_examples_two})
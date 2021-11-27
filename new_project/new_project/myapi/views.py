from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.http import Http404
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.
@api_view()
def detail(request, userid):
    try:
        person = Person.objects.get(userId=userid)
        serializer=PersonSerializer(person)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return Response(serializer.data)


@api_view()
def personALL(request):
    try:
        person = Person.objects.all()
        serializer=PersonSerializer(person, many=True)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return Response(serializer.data)
















































































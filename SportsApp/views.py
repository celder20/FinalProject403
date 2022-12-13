from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import footballlingo
from .forms import FootballLingoForm
from .views import * 

def SportLingoPageView(request) :
    data = footballlingo.objects.all()

    context = {
        'data': data
    }

    return render(request, 'FootballLingo/lingolist.html', context)

def UpdateLingoPageView(request, lingoid, term, description) :
    oldLingo = footballlingo.objects.get(lingoid = lingoid)

    oldLingo.term = term
    oldLingo.description = description

    oldLingo.save()
    return SportLingoPageView(request)

def DeleteTermPageView(request, lingoid):
    print(f'Deleting term {lingoid}')
    data = footballlingo.objects.get(lingoid = lingoid)

    data.delete()

    return SportLingoPageView(request)

def TermPageView(request, lingoid):
    data = footballlingo.objects.get(lingoid = lingoid)

    context = {
        'record': data
    }

    return render(request, 'FootballLingo/EditLingo.html', context)

def UpdateTermPageView(request):
    if request.method == 'POST':
        lingoid = request.POST['lingoid']

        oldTerm = footballlingo.objects.get(lingoid = lingoid)

        oldTerm.term = request.POST['term']
        oldTerm.description = request.POST['description']

        oldTerm.save()

    request.method = 'GET'
    return SportLingoPageView(request)

def AddTermPageView(request):
    if request.method == 'POST':
        newTerm = footballlingo()

        newTerm.term = request.POST['term']
        newTerm.description = request.POST['description']

        newTerm.save()
        
        return SportLingoPageView(request)
        
    else:
        SportLingoPageView(request)
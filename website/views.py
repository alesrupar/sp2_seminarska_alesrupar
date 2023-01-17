from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Events

# Create your views here.
#def index(request):
#    return render(request, 'index.html', {})

def index(request):
    events = Events.objects.all().values()
    template = loader.get_template('index.html')
    context = {
            'events': events,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addissue(request):
    x = request.POST['reported_by']
    z = request.POST['issue']
    w = request.POST['importance']
    newline = Events(reported_by=x, issue=z, importance=w)
    newline.save()
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    event  = Events.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
            'event': event,
    }
    return HttpResponse(template.render(context, request))

def editline(request, id):
    reported_by = request.POST['reported_by']
    issue = request.POST['issue']
    event = Events.objects.get(id=id)
    event.reported_by = reported_by
    event.issue = issue
    event.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    event = Events.objects.get(id=id)
    event.delete()
    return HttpResponseRedirect(reverse('index'))


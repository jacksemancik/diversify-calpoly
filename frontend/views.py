from django.shortcuts import render
from frontend.models import Content

def homepage(request):
    page = 1
    content = Content.objects.get(page=page)
    return render(request, 'introduction.html',{'content':content})

def institutional(request):
    page = 2
    content = Content.objects.get(page=page)
    return render(request, 'institutional.html', {'content':content,'text':textrender})

def state(request):
    page = 3
    content = Content.objects.get(page=page)
    return render(request, 'state.html', {'content':content})

def national(request):
    page = 4
    content = Content.objects.get(page=page)
    return render(request, 'national.html', {'content':content})

def references(request):
    page = 5
    content = Content.objects.get(page=page)
    return render(request, 'references.html', {'content':content})

def workscited(request):
    page = 0
    content = Content.objects.get(page=page)
    return render(request, 'workscited.html', {'content':content})

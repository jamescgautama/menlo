from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render



def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def check(request):
    query = request.GET.get('number')
    num = "{}".format(query)
    template = 'check.html'
    context = {
        'num': num,
    }
    return render(request, template, context)

def generate(request):
    query = request.GET.get('input')
    word = "{}".format(query)
    template = 'generate.html'
    context = {
        'word': list(word),
    }
    return render(request, template, context)

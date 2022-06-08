# from django.http import HttpResponse


# def detail(request, gig_name):
#     return HttpResponse("You're looking at gig %s." % gig_name)

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aboutUs(request):
    template = loader.get_template('about-us.html')
    context = {}
    return HttpResponse(template.render(context, request))
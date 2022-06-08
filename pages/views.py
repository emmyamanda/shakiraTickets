# from django.http import HttpResponse


# def detail(request, gig_name):
#     return HttpResponse("You're looking at gig %s." % gig_name)
import pymongo
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    client = pymongo.MongoClient("mongodb+srv://root:mjaFCaDuVWcYLybT@myfirstcluster.uaxcr.mongodb.net/?retryWrites=true&w=majority")
    db = client["shakira_tickets"]
    liveShows = db["live_shows"]
    context = {'liveShows': liveShows.find({})}

#    for show in liveShows.find():

    return HttpResponse(template.render(context, request))

def aboutUs(request):
    template = loader.get_template('about-us.html')
    context = {}
    return HttpResponse(template.render(context, request))

def liveShow(request, liveShow):
    template = loader.get_template('live-show-' + liveShow + '.html')
    context = {}
    return HttpResponse(template.render(context, request))
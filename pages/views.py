# from django.http import HttpResponse


# def detail(request, gig_name):
#     return HttpResponse("You're looking at gig %s." % gig_name)
import pymongo
from django.http import HttpResponse
from django.template import loader

def fetchLiveShowContext():
    client = pymongo.MongoClient("mongodb+srv://root:mjaFCaDuVWcYLybT@myfirstcluster.uaxcr.mongodb.net/?retryWrites=true&w=majority")
    db = client["shakira_tickets"]
    liveShows = db["live_shows"]
    context = {'liveShows': liveShows.find({})}
    return context


def index(request):
    liveShowsContext = fetchLiveShowContext()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(liveShowsContext, request))

def aboutUs(request):
    liveShowsContext = fetchLiveShowContext()
    template = loader.get_template('about-us.html')
    return HttpResponse(template.render(liveShowsContext, request))

def liveShow(request, liveShow):
    liveShowsContext = fetchLiveShowContext()
    template = loader.get_template('live-show-' + liveShow + '.html')
    return HttpResponse(template.render(liveShowsContext, request))
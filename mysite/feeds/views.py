# Create your views here.
#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson
import httplib2
import twitter
import jsonpickle

def index(request):
    api = twitter.Api(consumer_key='Ad3m2tX4qiwFvCEJw8HOOg',consumer_secret='Nzm3id4JGulXULeGVj2aiPWsxZxFvcXWuosr22D89AI',access_token_key='217970228-oc92QK9dInCRjuNE1dvxgPNuPC9dcvQh7uVPy5vB',access_token_secret='Oiru54uiWoe7GMYz59w0ykCf9IACi2s9zGRtWSWA8')
    # api = twitter.Api()
    statuses = api.GetUserTimeline(screen_name="fanzhang312", include_rts=False, include_entities=True, exclude_replies=True)

    status = jsonpickle.encode(statuses[:3])
    return HttpResponse(status, mimetype="application/json")
    
    # return render_to_response('feeds/index.html',{'latest_feed_list':statuses})
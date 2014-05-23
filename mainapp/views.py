import urllib2
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import json

# Create your views here.
def call(request):
	url = "	https://youtube-dl.appspot.com/api/info?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DnDS0Sr2Fhfk"
	try:
	  result = urllib2.urlopen(url)
	  data = json.load(result)
	  print(result)
	  return render_to_response('homepage.html', {
	  	'apicall':data['videos'][0]['formats'],
	  	'vidtitle' : data['videos'][0]['title'].replace (" ", "_")[:200]
	  	})
	except urllib2.URLError, e:
	  handleError(e)
	  return render_to_response('homepage.html')

# adata['videos'][0]['formats'][18]['format']



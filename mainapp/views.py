import urllib2
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import json


# Create your views here.
def call(request):
	print (request)
	link = request.POST.get('link')
	url = "https://youtube-dl.appspot.com/api/info?url="+link
	try:
	  result = urllib2.urlopen(url)
	  data = json.load(result)
	  return render_to_response('api.html', {
	  	'apicall':data['videos'][0]['formats'],
	  	'vidtitle' : data['videos'][0]['title'].replace (" ", "_")[:200],
	  	})
	except urllib2.URLError, e:
	  print(e)
	  return render_to_response('homepage.html')

# adata['videos'][0]['formats'][18]['format']



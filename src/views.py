from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def pics(request):

	map_url = 'http://maps.googleapis.com/maps/api/geocode/json?address='+request.GET.get('location','')
	content = urllib.request.urlopen(map_url)
	data = content.read()
	map_json = json.loads(data.decode("utf8"))
	latitude = map_json['results'][0]['geometry']['location']['lat']
	longitude = map_json['results'][0]['geometry']['location']['lng']

	instagram_url = 'https://api.instagram.com/v1/media/search?lat='+str(latitude) +'&'+'lng='+str(longitude)+'&distance=5000&client_id=8744f907857d4da88c2c8f16adb9b204'
	instagram_content = urllib.request.urlopen(instagram_url)
	instagram_data = instagram_content.read()
	instagram_json = json.loads(instagram_data.decode("utf8"))
	 
	return render(request, 'pics.html',{'instagram_json':instagram_json})
	# return render(request, 'pics.html',{'latitude':latitude,'longitude':longitude})
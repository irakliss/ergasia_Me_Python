import urllib2
import json
import requests


def send_simple_message(inputtext,inputmail):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox859bf6aed7914f92a5b7c899e7579dc8.mailgun.org/messages",
        auth=("api", "key-d81acf0fb3a600ead848434314d983e9"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox859bf6aed7914f92a5b7c899e7579dc8.mailgun.org>",
              "to":inputmail,
              "subject": "Hello Iraklis Skourtis",
			"text":inputtext})
			
						

email=input("Give me your mail ")

						
url = 'https://api.punkapi.com/v2/beers/random'

request = urllib2.Request(url)

headers = {"Content-Type":"application/json"}
for key,value in headers.items():
    request.add_header(key,value)            


res = urllib2.urlopen(request).read()
data = json.loads(res)

msgText = "NAME :: " + data[0]['name'].encode("utf-8")

msgText = msgText + "\r\nTAGLINE :: " + data[0]['tagline'].encode("utf-8") + "\r\n\r\n"

msgText = msgText + data[0]['description'].encode("utf-8")

send_simple_message(msgText,email)
import json
import sys
import urllib2
import re
from bs4 import BeautifulSoup

def main() :
	# setting variables at the top

	json = {"mentions":[], "emoticons":[], "links":[]}

	values = sys.argv[1].split(" ")

	for string in values :
		length = len(string)

		# if string is all letters, doesn't fit any condition
		if string.isalpha() :
			continue

		elif string[0] == "@" and string[1:length].isalpha() :
			
			json["mentions"].append(string[1:length])

		elif string[0] == "(" and string[length-1] == ")" and string[1:length-1].isalpha() :
			
			json["emoticons"].append(string[1:length-1])

		else :

			result = handleUrls(string)

			if result :
				json["links"].append(result)


	print json

# @var string
# determines if string is url
# returns dictionary with structure { url: [url string], title: [url title]}
def handleUrls(string) :

	links = {}

	url_list = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)

	if len(url_list) :
		
		links["url"] = string

	else :
		
		return None

	response = urllib2.urlopen(string)
	html = response.read()

	soup = BeautifulSoup(html)
	title = soup.html.head.title


	links["title"] = title.contents

	return links




main()
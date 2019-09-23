#!/usr/bin/env python3

import os
import time
import requests
import copy
import json

stat_dict = {
    "url": "",
    "html text": "",
    "random number": "",
    "request time": ""
}

website_dict = {
    "python-vm": copy.deepcopy(stat_dict),
    "python-appengine": copy.deepcopy(stat_dict),
    "java-vm": copy.deepcopy(stat_dict),
    "java-appengine": copy.deepcopy(stat_dict)
}

website_dict["python-vm"]["url"] = "http://35.209.210.228:5000"
website_dict["python-appengine"]["url"] = "http://moonlit-sphinx-253117.appspot.com"
website_dict["java-vm"]["url"] = "http://35.209.210.228:9999/randomNumber/randNum"
website_dict["java-appengine"]["url"] = "http://randomnum.appspot.com"

if not os.path.exists("webscraper-results"):
    os.mkdir("webscraper-results")

for website_type, stat_dict in website_dict.items():

    start_time = time.time()
    url_request = requests.get(stat_dict["url"])
    end_time = time.time()
    total_time = end_time - start_time
    html_text = url_request.text

    website_dict[website_type]["html text"] = html_text
    website_dict[website_type]["request time"] = total_time

    with open("webscraper-results/" + website_type + ".txt", "w") as f:
        f.write(json.dumps(website_dict[website_type]))

print("Success! See webscraper-results directory for result text files")

#!/usr/bin/env python3

import os
import time
import requests
import copy
import json
import socket

def get_website_string(website):
    current_name = socket.gethostname()
    current_ip = socket.gethostbyname(current_name)
    str = "From current address {}: {}_{}_{}_{}@{} {} {}\n\n".format(current_ip, website["region"], website["zone"], website["server type"], website["language"], website["url"], website["request time"], website["html text"])

    return str

website_list = []
python_vm_us = {
    "language": "Python",
    "server type": "VM",
    "region": "us-central1",
    "zone": "a",
    "url": "http://35.209.210.228:5000"
}
website_list.append(python_vm_us)

python_app_us = {
    "language": "Python",
    "server type": "app",
    "region": "us-central1",
    "zone": "a",
    "url": "http://moonlit-sphinx-253117.appspot.com"
}
website_list.append(python_app_us)

python_vm_aussie = {
    "language": "Python",
    "server type": "VM",
    "region": "australia-southeast1",
    "zone": "a",
    "url": "http://35.244.66.146:5000"
}
website_list.append(python_vm_aussie)

python_app_aussie = {
    "language": "Python",
    "server type": "app",
    "region": "australia-southeast1",
    "zone": "a",
    "url": "http://timing-experiment-flask.appspot.com/"
}
website_list.append(python_app_aussie)

java_vm_us = {
    "language": "Java",
    "server type": "VM",
    "region": "us-central1",
    "zone": "a",
    "url": "http://35.209.210.228:9999/randomNumber/randNum"
}
website_list.append(java_vm_us)

java_app_us = {
    "language": "Java",
    "server type": "app",
    "region": "us-central1",
    "zone": "a",
    "url": "http://randomnum.appspot.com"
}
website_list.append(java_app_us)

java_vm_aussie = {
    "language": "Java",
    "server type": "VM",
    "region": "australia-southeast1",
    "zone": "a",
    "url": ""
}

java_app_aussie = {
    "language": "Java",
    "server type": "app",
    "region": "australia-southeast1",
    "zone": "a",
    "url": "http://randomnumzonea.appspot.com/"
}
website_list.append(java_app_aussie)

if not os.path.exists("webscraper-results"):
    os.mkdir("webscraper-results")

for website in website_list:

    start_time = time.time()
    url_request = requests.get(website["url"])
    end_time = time.time()
    total_time = end_time - start_time
    html_text = url_request.text

    website["html text"] = html_text
    website["request time"] = total_time

    with open("webscraper-results/{}_{}_{}_{}.txt".format(website["region"], website["zone"], website["server type"], website["language"]), "w") as f:
        f.write(get_website_string(website))

print("Success! See webscraper-results directory for result text files")

#!/usr/bin/env python3
# hello_world.py

import sys
import random
sys.path.append("../webserver-python/")

from flask import Flask
app = Flask(__name__)

from random_generator import generator_wrapper

phrase_list = [
    "Wot the fuck m8",
    "Get off this website d00d",
    "u suck",
    "if you're reading this, the treasure is under the clocktower",
    "bitch plz"
    ]

@app.route('/')
def hello_world():
    generator = generator_wrapper()
    sample = next(generator)
    phrase_choice = random.choice(phrase_list)

    insert_var = sample
    if sample % 2 == 0:
        insert_var = phrase_choice

    return "<h1>Random number: {}</h1><h1>Reload the page for a new number!</h1>".format(insert_var)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

#!/usr/bin/env python3

import time
import sys

from random_generator import generator_wrapper

html_base_file_path = "../docs/base.html"
html_base_file = open(html_base_file_path, "r")

html_index_file_path = "../docs/index.html"
html_index_file = open(html_base_file_path, "r+")

generator = generator_wrapper()

var_string = "variable"
while True:

    sample = str(next(generator))
    html_text = html_base_file.read()
    html_base_file.seek(0, 0)
    html_text = html_text.replace(var_string, sample)

    html_index_file = open(html_index_file_path, "w")
    html_index_file.write(html_text)
    html_index_file.close()

    print(html_text)

    time.sleep(1)

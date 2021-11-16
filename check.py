import numpy as np
import pandas as pd
import re # Regular Expressions
from collections import Counter
import string
import enchant
from flask import *
from flask import render_template






def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        words = []
        for line in text:
            words = words + re.findall(r'\w+', line.lower()) # RE for making a words list from file
            
    return words        

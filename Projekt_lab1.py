# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:41:54 2021

@author: weron
"""
import argparse
from collections import Counter
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor

parser = argparse.ArgumentParser(description = "Opis")

parser.add_argument('-file', help='file name', default = 'WinnieThePooh.txt')
parser.add_argument('-w', '--words', help = 'Number of words', type = int, default=10)
parser.add_argument('-l', '--letters', help = 'Min length of word', type = int, default=0)

args = parser.parse_args()

with open(args.file, encoding='utf8') as f:
    data = f.read().strip().split()
    counts = Counter(data)
    #print(counts)

sort = sorted(counts.items(), key = lambda e: e[1], reverse = True)

graph = Pyasciigraph(
    min_graph_length = 70,
    separator_length = 2)

pattern = [Yel, Gre, Blu, Red, Cya, Pur]
data = vcolor(sort, pattern)

i = 0
for line in graph.graph(label = "Histogram of the greatest number of words in the text", data = data):
    if i <= args.words:
        print(line)
        i += 1
    else:
        break
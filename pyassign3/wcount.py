#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Liuziyu"
__pkuid__  = "1700011766"
__email__  = "1700011766@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    
    a = lines.lower()
    for c in a:
        if c.isalpha():
            pass
        else:
            a = a.replace(c," ")
    a = a.split()
    f = {}
    for d in a:
        f[d] = f.get(d, 0) + 1
    g = sorted(f.items(), key=lambda kv:kv[1],reverse=True)
    for n in range(topn):
        i, j = g[n]
        print(i, '\t', j)
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

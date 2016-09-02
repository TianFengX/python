#!/usr/bin/python
#coding=utf-8
#0004.py
#author:TianFengX
#function:statistic one English file words

#import re
from collections import Counter

def main():
    print("0004.py main")
    with open('test.txt') as my_file:
	cnt = Counter()
	for line in my_file:
	    words = line.split()
	    cnt += Counter(words)
	for words in cnt.most_common():
	    print(words)

if __name__ == "__main__":
    main()
else:
    print("0004.py was imported !")

